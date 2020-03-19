# Graph DBs

- directed property graphs have:
  - nodes/vertices (things)
  - edges (relationships)
  - properties (attributes of node/edge)

## TinkerGraph: in memory graph

```groovy
:remote connect tinkerpop.server conf/remote.yaml
:load /Users/jordan/Development/graph/sample-data/load-air-routes-graph.groovy
:load /Users/jordan/Development/rethink/load-graph.groovy
```

or

```groovy
graph = TinkerGraph.open()
g = graph.traversal()
```

```groovy
g.V().hasLabel('airport')
g.V().has('airport','code','DFW').values()
g.V().has('airport','code','DFW').values('runways','icao')
g.V().has('region')
g.V().hasNot('region')
g.V().hasLabel('airport').count()

g.V().has('code','AUS').valueMap().unfold()
g.V().has('code','AUS').elementMap().unfold()

// How many of each type of vertex are there?
g.V().groupCount().by(label)

// where can I fly from Austin?
g.V().has('airport','code','AUS').out().values('code').fold()
g.V().has('airport','code','AUS').out('route').values('code').fold()

// get the path...
g.V().has('airport','code','LCY').outE().inV().path()

g.V().has('airport','code','AUS').out().out().path().by('code').limit(10)

// check if edge exists between nodes
g.V().has('code','AUS').out('route').has('code','DFW').hasNext()

// get edge between vertices and get property value
g.V().has('code','MIA').outE().as('e').inV().has('code','DFW').select('e').values('dist')

// Only return the FIRST 20 results
g.V().hasLabel('airport').values('code').limit(20)

// Only return the LAST 20 results
g.V().hasLabel('airport').values('code').tail(20)

// Only return the FIRST 20 results
g.V().hasLabel('airport').range(0,20).values('code')

g.V().has('region','GB-ENG').values('runways').dedup().fold()

g.V().has('code','DFW').id()
g.V().hasId(8).values('code')

g.V().hasLabel('airport').values('runways').sum()
g.V().has('runways',gte(5)).values('code','runways').fold()
g.V().hasLabel('airport').has('city',startingWith('X')).values('city')

g.V().and(has('code','AUS'),has('icao','KAUS'))
g.V().has('airport','code','LHR').out().count()
```

## Adding vertices

```groovy
// Add an imaginary airport with a code of 'XYZ' and connect it to DFW
xyz = g.addV('airport').property('code','XYZ').
                        property('icao','KXYZ').
                        property('desc','This is not a real airport').next()

// Add a route from DFW to XYZ
g.V().has('code','DFW').addE('route').to(xyz)

// Add the return route back to DFW
g.V().has('code','DFW').addE('route').from(xyz)

// check if exists
g.V().has('code','XYZ').fold()
// add if not exists
g.V().has('code','XYZ').fold().coalesce(unfold(),addV().property('code','XYZ'))
// upsert with property
g.V(3).fold().
       coalesce(unfold().property('runways',3),
       addV('airport').property('runways',3))
```

## Updating properties

```groovy
g.addV('country').property('timestamp', new Date());
g.V().hasLabel('country').property(single,'timestamp', new Date());
```

## drop vertex/edge

```groovy
g.V().has('code','XYZ').drop()
// Remove the flight from AUS to LHR  (both directions).
g.V().has('code','AUS').outE().as('e').inV().has('code','LHR').select('e').drop()
g.V().has('code','LHR').outE().as('e').inV().has('code','AUS').select('e').drop()

// drop ALL edges
g.E().drop()
// Delete the entire graph!
g.V().drop()
```

## drop property

```groovy
g.V().has('code','SFO').properties('desc').drop()
g.V().has('code','SFO').properties().drop()
```

```xml
  <node id='1'>
    <data key='labelV'>airport</data>
    <data key='type'>airport</data>
    <data key='code'>ATL</data>
    <data key='icao'>KATL</data>
    <data key='city'>Atlanta</data>
    <data key='desc'>Hartsfield - Jackson Atlanta International Airport</data>
    <data key='region'>US-GA</data>
    <data key='runways'>5</data>
    <data key='longest'>12390</data>
    <data key='elev'>1026</data>
    <data key='country'>US</data>
    <data key='lat'>33.6366996765137</data>
    <data key='lon'>-84.4281005859375</data>
  </node>
  <edge id='37622' source='1039' target='702'>
    <data key='labelE'>route</data>
    <data key='dist'>275</data>
  </edge>
```

## Loading sample data

Modify path to reflect location of data file.

`load-air-routes-graph.groovy`

```groovy
// You can use this file to load the air-routes graph from the Gremlin Console
//
// To execute use the console command ":load load-air-routes-graph.groovy"
//

conf = new BaseConfiguration()
conf.setProperty("gremlin.tinkergraph.vertexIdManager","LONG")
conf.setProperty("gremlin.tinkergraph.edgeIdManager","LONG")
conf.setProperty("gremlin.tinkergraph.vertexPropertyIdManager","LONG")
graph = TinkerGraph.open(conf)

// Change the path below to point to wherever you put the graphml file
graph.io(graphml()).readGraph('/Users/jordan/Development/graph/sample-data/air-routes.graphml')

g=graph.traversal()
:set max-iteration 1000
```

## Gremlin python

```python
nodes = g.V(source_id).outE().hasLabel(relationship).inV().has( 'admin_flagged', False).has('flagged_count', inside(0, FLAG_COUNT_THRESHOLD)).as_('v').select('v').fold().next()
```

Imports:

```python
from chalice import Chalice
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.process.traversal import T, P, Operator, Cardinality
```

CORS

```python
@admin.route('/status', methods=['GET'], cors=True)
def status():
    try:
        graph.g.V().limit(0).fold().next()
    except ConnectionRefusedError as e:
        raise ChaliceViewError(e)
    return {'status': 'OK'}
```

Manual auth

```python
def decode_and_verify_token(token):
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']

    key_index = -1
    for i in range(len(cognito_keys)):
        if kid == cognito_keys[i]['kid']:
            key_index = i
            break
    if key_index == -1:
        raise BadRequestError('Public key not found in jwks.json')

    public_key = jwk.construct(cognito_keys[key_index])
    message, encoded_signature = str(token).rsplit('.', 1)
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))

    if not public_key.verify(message.encode("utf8"), decoded_signature):
        raise BadRequestError('Signature verification failed')

    app_client_id = os.environ.get('APP_CLIENT_ID')
    claims = jwt.get_unverified_claims(token)
    # additionally we can verify the token expiration
    if time.time() > claims['exp']:
        raise BadRequestError('Token expired')
    # and the Audience (use claims['client_id'] if verifying an access token)
    if claims['aud'] != app_client_id:
        raise BadRequestError('Token was not issued for this audience')

    return claims
```