# JS

## ES6

### var, let, const

```js
var a = 1;
a = 2;
var a = 3;

let b = 1;
b = 2;

const c = 1;
```

- var, let, const are scoped to parent function
- let and const are block scoped (for, if), var is not

### Strings

- template literals:

```js
const s = `Hi, my name is ${name}`;
// startsWith, endsWith, includes
const j = s.startsWith('j');
const manyJ = s.repeat(5);
```

### Arrow function

- uses `this` of surrounding scope

```js
function square(x) {
  return x * x;
}
const square = function(x) {
  return x * x;
};
const square = x => {
  return x * x;
};
const square = x => x * x;
```

### Destructuring

```js
const [, two = 2] = [1, 2, 3];
console.info(one, two);

const person = {
  name: 'jordan',
  age: 31,
  location: {
    city: 'Victoria',
    temp: 22,
  },
};

const { name: firstName = 'anon', age = 0, location } = person;
const { city, temp: temperature } = location;

console.info(age, firstName);
console.info(city, temperature);

const calc = year => {
  return [123, 456]
}
const [a, b] = calc(1988)
```

### Arrays

```js
for (const cur of arr) {
  if (cur > 0) break;
}

arr.forEach(x => {
  f(x);
});
```

### Spread Operator

```js
const addNums = (a, b, c, d, e) => a + b + c + d + e;
const nums = [2, 3, 5, 7, 11];
const res = addNums(...nums);

const a = [1, 2];
const b = [3, 4];
const c = [...a, ...b];
```

### Rest Parameters

- turn input into array

```js
const f = (...years) => {};
f(1, 2, 3);
```

### Default Parameters

```js
const f = (a, b, c = 0) => {};
```

### Maps

- Maps are general purpose hash maps
- can use num/string/bool/functions/objects as keys

```js
const m = new Map();
m.set('k', 314);
m.has('k');
m.get('k');
m.delete('k');
m.clear();
```

### Classes

```js
class Person {
  constructor(age) {
    this.age = age;
  }
  calcAge() {}
  static hello() {
    console.info('hi');
  }
}
const jordan = new Person(31);
Person.hello();

class Athlete extends Person {
  constructor(age, sport) {
    super(age);
    this.sport = sport;
  }
}
```

#### Class Properties

```js
class OldSyntax {
  constructor() {
    this.name = 'jordan';
  }
  getGreeting() {
    return `I'm ${this.name}`;
  }
}

class NewSyntax {
  name = 'jordan';
  getGreeting = () => {
    return `I'm ${this.name}`;
  };
}
```

### Import, Export

```js
const square = x => x * x;
const add = (a, b) => a + b;
export { square, add };
```

```js
export const square = x => x * x;
export const add = (a, b) => a + b;
```

```js
import { square, add } from './utils';
```

#### Default Export

```js
const add = (a, b) => a + b;
const sub = (a, b) => a - b;

export { add, sub as default };
```

```js
export default (a, b) => a - b;
```

```js
import subtract, { add } from './utils';
```

## ES6 Async

- stuff like `setTimeout()`, DOM events, http requests are Web APIs, they run in the Web API env parallel to the exec stack!
- the callback goes on message queue when event occurs
- the event loop monitors message queue and moves these items onto exec stack
- can use callback chaining (callback hell) to ensure order of async

### Promises

- object that keeps track of async events
- pending -> settled/resolved: fulfilled | rejected

```js
const getIDs = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve([314, 217, 676]);
  }, 1500);
});

const getRecipe = recID => {
  return new Promise((resolve, reject) => {
    setTimeout(
      id => {
        const recipe = {
          title: 'pizza',
          publisher: 'jordan',
        };
        resolve(`${id}, ${recipe.title}, ${recipe.publisher}`);
      },
      1500,
      recID
    );
  });
};

const getRelated = publisher => {
  return new Promise((resolve, reject) => {
    setTimeout(
      pub => {
        const recipe = {
          title: 'chili',
          publisher: 'jordan',
        };
        resolve(`${pub}: ${recipe.title}`);
      },
      1500,
      publisher
    );
  });
};

getIDs
  .then(ids => {
    console.info(ids);
    return getRecipe(ids[0]);
  })
  .then(recipe => {
    console.info(recipe);
    return getRelated('jordan');
  })
  .then(recipe => {
    console.info(recipe);
  })
  .catch(err => {
    console.info(err);
  });
```

### Async/Await ES8

```js
// replace getIDs part above with:
async function getRecipesAW() {
  const ids = await getIDs;
  const recipe = await getRecipe(ids[0]);
  const related = await getRelated('jordan');
  return related;
}
getRecipesAW().then(res => console.info(res));
```

### AJAX (async js and xml)

```js
fetch('https://httpbin.org/get')
  .then(result => {
    return result.json();
  })
  .then(data => console.info(data))
  .catch(err => console.info(err));
```

- using async await

```js
async function getStuff() {
  try {
    const result = await fetch('https://httpbin.org/get');
    const data = await result.json();
    return data;
  } catch (err) {
    console.info(err);
  }
}
let apiData;
getStuff().then(data => {
  apiData = data;
  console.info(apiData);
});
```

## Types and Variables

- primitives: numbers, strings, bools, undefined, null
- objects: arrays, functions, objects, dates, wrappers
- dynamic typing (figures out type when you assign)
- type coercion (num to string when concating to string)
- `typeof myName`

## Conditionals, Ternary, Truthy

- `a===b` exact equals
- `if ( 18 < age && age < 99) {}`
- `var drink = age >= 18 ? 'beer' : 'juice';`
- falsy values: `undefined, null, 0, '', NaN`
- truthy values: every other value

## Args and this

- arrow functions do not have access to `arguments` objects in function
- `this` is no longer bound, it is grabbed from parent scope

```js
const user = {
  data: ['jordan', 'vic'],
  printName() {
    console.info(this.name);
    this.data.forEach(function(thing) {
      console.info(this.name, thing); // won't work
    });
  },
};
const user = {
  data: ['jordan', 'vic'],
  printName() {
    console.info(this.name);
    this.data.forEach(thing => {
      console.info(this.name, thing); // does work
    });
  },
};
```

## Map

- the original array is NOT modified!

```js
const nums = [2, 3, 5, 7];
const squares = nums.map(num => num * num);
```

## Execution Contexts

- all JS runs in some execution context
- the default exec context is the Global one
- `myVar === window.myVar` -> true (for browsers)
- top level vars are stuck onto the global object
- each function creates a new exec context
- function calls get added to execution stack

### Creation Phase

1. The Variable Object is created

- argument object is created (contains all args passed in)
- code is scanned for f'n declarations: for each f'n a property is created in the VO pointing to the f'n (hoisting)
- code is scanned for variable declarations: for each var a property is created in the VO and set to _undefined_ (hoisting)

```js
// function declaration -> this will work
f();
function f() {}
// function expression -> this will not work (undefined)
t();
const t = () => {};
```

2. The scope chain is created (where we can access certain vars)

- each f'n creates a new scope
- lexical scoping (position of the var determines scope)
- nested f'ns creates a scope chain -- js will search up the chain for the vars
- nesting determines scope, lexical order determines exec stack order

```js
var a = 1;
function a() {
  var b = 2;
  function b() {
    var c = 3;
    console.info(a + b + c);
  }
}
```

3. The value of `this` var is determined

- in regular exec context this points to global object (`window`)
- in method calls `this` points to the object calling it
- in f'n calls `this` points to the global object, its parent

### Execution Phase

1. Code of the function that created the current context is run line by line

## DOM (document object model)

- Javascript manipulates the DOM
- head and body

```js
// selects the first item it finds!
document.querySelector('#my-thing').textContent = 'text';
document.querySelector('.thing').style.display = 'none';
```

## Events

- events are notifications sent to notify the js that something happened on page
- event listeners do stuff based on these events
- events are only handled once execution stack is empty
- events go into the _message queue_, when the exec stack is empty the associated handler function goes onto the exec stack and gets executed

```js
document.querySelector('.thing').addEventListener('click', () => {});
var diceDOM = document.querySelector('thing');
diceDOM.style.display = 'block';
```

## Objects and Functions

- almost everything is an object
- primitives: numbers, strings, bools, undefined, null
- objects: arrays, functions, objects, dates, wrappers

- all objects have a prototype property which enables inheritance
- the prototype property is where we put methods and properties we want others to inherit
- constructors prototype property is not the prototype of the constructor, but of everything we create through it

- every object we create is an instance of the object object
- our objects inherit these methods (hasOwnProperty(), toString(), etc.)
- if we call a method JS will search up the prototype chain for it
- the final thing in the chain is `null`, which has no methods

```js
var Person = function(name, yearOfBirth) {
  this.name = name;
  this.yearOfBirth = yearOfBirth;
};
var jordan = new Person('jordan', 1988);
var taylor = new Person('taylor', 1986);
// these additions will be inherited by all
Person.prototype.calculateAge = function() {};
Person.prototype.lastName = 'smith';
```

- `new` points `this` to the empty object rather than global object

### Primitives vs Objects

- variable for an object holds a _pointer_ to that object in memory
- variable for a primitive actually holds the value

### Function

- First-class functions: function are objects, can be passed as args, returned from functions, etc

```js
function interviewQuestion(job) {
  if (job === 'designer') {
    return function(name) {};
  } else {
    return function(name) {};
  }
}
```

### IIFE (immediately invoked function expression)

```js
(function(input) {
  console.info(input);
})('test string');
```

### Closures

- the inner function is able to use the `retirementAge` variable and the `a` variable even though the function execution has stopped once the function is returned
- an inner function always has access to variables and params of outer function even after outer function has returned -- the scope chain stays intact

```js
function retirement(retirementAge) {
  var a = ' years left until retirement';
  return function(yearOfBirth) {
    console.info(retirementAge - (2019 - yearOfBirth) + a);
  };
}
var retirementUS = retirement(66);
retirementUS(1990);
retirement(66)(1990);
```

### Bind, Call, Apply

- Method borrowing: we can pass in a new `this` using `call` method
- Currying: create function based on another function with some presets

```js
var jordan = {
  name: 'jordan',
  presentation: function(style, timeOfDay) {
    if (style === 'formal') {
    }
  },
};
var emily = {
  name: 'emily',
};
jordan.presentation.call(emily, 'formal', 'noon');
// won't actually work here
jordan.presentation.apply(emily, ['formal', 'noon']);
jordan.presentation.bind(emily, ['formal']);
var jordanFormal = jordan.presentation.bind(jordan, 'formal');
jordanFormal('noon');
```

## Webpack

### Loaders

Loaders process files. So you can run your JS files through the loader and it will compile it down to ES5 or w/e.
