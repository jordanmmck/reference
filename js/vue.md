# Vue

Vue has a virtual DOM. The Vue instance checks for differences against the virtual DOM. If the instance detects the virtual DOM is out of date, it updates the virtual DOM and propagates that update to the actual DOM.

## hello world ++

```html
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
  <input type="text" v-on:input="changeTitle" />
  <p>{{title}}</p>
</div>
```

```js
new Vue({
  el: "#app",
  data: {
    title: "ETHEREUM TO $100K",
  },
  methods: {
    changeTitle: function (event) {
      this.title = event.target.value;
    },
  },
});
```

## setting html tag attributes

```html
<div>
  <img v-bind:src="img-src" />
</div>
<a v-bind:href="link">my link</a>
```

## event listening

Check out the `.enter` modifier below. More [here](https://vuejs.org/v2/api/?#v-on).

```html
<div id="app">
  <button v-on:click="increment(2, $event)">click</button>
  <button v-on:click="counter++">click</button>
  <p>{{counter}}</p>
  <p v-on:mousemove="updateCoords">
    {{x}}/{{y}}
    <span v-on:mousemove.stop="">DEAD SPOT</span>
  </p>
  <input type="text" v-on:keyup.enter="alertMe" />
  <input type="text" v-on:keydown="myValue=$event.target.value" />
</div>
```

```js
new Vue({
  el: "#app",
  data: {
    myValue: "",
    counter: 0,
    x: 0,
    y: 0,
  },
  methods: {
    increment: function (step, event) {
      this.counter += step;
    },
    updateCoords: function (event) {
      this.x = event.clientX;
      this.y = event.clientY;
    },
    alertMe: function () {
      alert("yo");
    },
  },
});
```

## 2-way binding

```html
<script src="https://npmcdn.com/vue/dist/vue.js"></script>

<div id="app">
  <input type="text" v-model="name" />
  <p>{{name}}</p>
</div>
```

```js
new Vue({
  el: "#app",
  data: {
    name: "JORDAN",
  },
});
```

## methods, computed, watch

### methods

## computed

These properties are accessed like properties that you use in your app like `data`. They are re-computed as necessary.

Computed tasks are always run synchronously! No HTTP requests!

```html
<div id="app">
  <button v-on:click="count++">+</button>
  <button v-on:click="count--">-</button>
  <button v-on:click="secondCount++">++</button>
  <p>counter: {{ count }}</p>
  <p>result: {{ result() }}</p>
</div>
```

```js
new Vue({
  el: "#app",
  data: {
    count: 0,
    secondCount: 0,
  },
  computed: {
    result() {
      return this.count > 5 ? "greater" : "smaller";
    },
  },
});
```

If you click the button that increments `secondCount`, Vue will re-run the `result` function on the page because it doesn't know whether it used the `secondCount` variable.

To prevent this:

```html
<div id="app">
  <button v-on:click="count++">+</button>
  <button v-on:click="count--">-</button>
  <button v-on:click="secondCount++">++</button>
  <p>counter: {{ count }}</p>
  <p>result: {{ result() | {{ output }}} }</p>
</div>
```

```js
new Vue({
  el: "#app",
  data: {
    count: 0,
    secondCount: 0,
  },
  computed: {
    output() {
      return this.count > 5 ? "greater" : "smaller";
    },
  },
  methods: {
    result() {
      return this.count > 5 ? "greater" : "smaller";
    },
  },
});
```

## watch

Watch for changes to something in `data` and execute some code when a change happens.

```js
new Vue({
  el: "#app",
  data: {
    count: 0,
  },
  watch: {
    count: function (value) {
      var vm = this;
      setTimeout(function () {
        vm.count = 0;
      }, 2000);
    },
  },
});
```

## looping

```html
<div id="app">
  <ul>
    <li v-for="num,i in nums">the {{i}}th prime: {{num}}</li>
  </ul>
</div>
```

```js
new Vue({
  el: "#app",
  data: {
    nums: [2, 3, 5, 7, 11, 13],
  },
});
```
