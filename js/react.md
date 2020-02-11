# React

```zsh
yarn global add live-server
live-server public
```

## General Notes

- React components update when `props` or `state` changes

## JSX (Javascript extension language)

- ReactDOM renders JSX
- Render wants some JSX and a place to inject

```js
ReactDOM.render(template, appRoot);
```

## Babel

- Compiles fancy JS to ES5
- Compiles JSX to JS

```zsh
yarn global add babel-cli
yarn init
yarn add babel-preset-react
yarn add babel-preset-env
```

Use babel...

```zsh
babel src/app.js --out-file=public/scripts/app.js --presets=env,react --watch
live-server public
```

## Conditional Rendering

```jsx
<p>{getLocation()}</p>;
// in function: return <p>Location: {location}</p>
{
  getLocation(user.location);
}
<h1>{user.name ? user.name : 'Anon'}</h1>;
{
  user.age >= 18 && <p>Age: {user.age}</p>;
}
{
  user.age && user.age >= 18 && <p>Age: {user.age}</p>;
}
```

## Forms

```jsx
const onFormSubmit = e => {
  e.preventDefault();
  const option = e.target.elements.option.value;
};
// ...
<form onSubmit={onFormSubmit}>
  <input type="text" name="option" />
  <button>Add Option</button>
</form>;
```

## Components

```jsx
class Options extends React.Component {
  render() {
    return (
      <div>
        <Option />
      </div>
    );
  }
}
```

### this binding

- instead of doing this binding on methods, just make them arrow functions!

```jsx
class Options extends React.Component {
  constructor(props) {
    super(props);
    this.handleRemoveAll = this.handleRemoveAll.bind(this);
  }

  handleRemoveAll() {
    console.info(this.props.options);
  }

  render() {
    return (
      <div>
        <button onClick={this.handleRemoveAll}>Remove All</button>
      </div>
    );
  }
}
```

### Component state

```jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.handleAddOne = this.handleAddOne.bind(this);
    this.state = {
      count: 0,
    };
  }
  handleAddOne() {
    this.setState(prevState => ({ count: prevState.count + 1 }));
  }
  render() {
    return (
      <div>
        <h1>Count: {this.state.count}</h1>
        <button onClick={this.handleAddOne}>+1</button>
      </div>
    );
  }
}

ReactDOM.render(<Counter />, document.getElementById('app'));
```

### Passing method to Component

```jsx
class IndecisionApp extends React.Component {
  handleDeleteOptions() {}

  render() {
    return (
      <div>
        <Options handleDeleteOptions={this.handleDeleteOptions} />
      </div>
    );
  }
}

class Options extends React.Component {
  render() {
    return (
      <div>
        <button onClick={this.props.handleDeleteOptions} />
      </div>
    );
  }
}
```

### Passing data up

```jsx
class IndecisionApp extends React.Component {
  constructor(props) {
    super(props);
    this.handleAddOption = this.handleAddOption.bind(this);
    this.state = {
      options: ['one', 'two', 'three', 'four'],
    };
  }
  handleAddOption(option) {
    this.setState(prevState => ({ options: prevState.options.concat(option) }));
  }

  render() {
    return (
      <div>
        <AddOption handleAddOption={this.handleAddOption} />
      </div>
    );
  }
}

class AddOption extends React.Component {
  constructor(props) {
    super(props);
    this.handleAddOption = this.handleAddOption.bind(this);
  }

  handleAddOption(e) {
    e.preventDefault();
    const option = e.target.elements.option.value.trim();
    e.target.elements.option.value = '';
    if (option) {
      this.props.handleAddOption(option);
    }
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleAddOption}>
          <input type="text" name="option" />
          <button>Add Option</button>
        </form>
      </div>
    );
  }
}
```

### Props and state

#### Props

- object
- can be used when rendering
- changes from above cause re-render
- comes from above
- can't be changed by component itself

#### State

- object
- can be used when rendering
- changes cause re-render
- defined in component itself
- can be changed by component itself

#### Props.children

```jsx
const Layout = props => {
  return (
    <div>
      <p>header</p>
      {props.children}
      <p>footer</p>
    </div>
  );
};

ReactDOM.render(
  <Layout>
    <div>
      <h1>Title</h1>
      <p>CONTENT</p>
    </div>
  </Layout>,
  document.getElementById('app')
);
```

### Stateless Functional Components

- stateless f'n components do not have lifecycle methods

```jsx
const Header = props => {
  return (
    <div>
      <h1>{props.title}</h1>
      <h2>Trust the Computer</h2>
    </div>
  );
};
```

### Default props

```jsx
const Header = props => {
  return (
    <div>
      <h1>{props.title}</h1>
      <h2>Trust the Computer</h2>
    </div>
  );
};

Header.defaultProps = {
  title: 'Indecision',
};
```

### Lifecycle Methods

```js
  componentDidMount() {
    console.info('did mount');
  }
  componentDidUpdate(prevProps, prevState) {
    console.info('did update');
  }
  componentWillUnmount() {
    console.info('will unmount');
  }
```

## localStorage

- only saves strings

```jsx
localStorage.setItem('key', 'value');
```

## Source map

- get actual error location rather than bundle.js

## Routing

```jsx
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import AddExpensePage from '../components/AddExpensePage';
import EditExpensePage from '../components/EditExpensePage';
import ExpenseDashboardPage from '../components/ExpenseDashboardPage';
import Header from '../components/Header';
import HelpPage from '../components/HelpPage';
import NotFoundPage from '../components/NotFoundPage';

const AppRouter = () => (
  <BrowserRouter>
    <Header />
    <Switch>
      <Route path="/" exact component={ExpenseDashboardPage} />
      <Route path="/create" component={AddExpensePage} />
      <Route path="/edit/:id" component={EditExpensePage} />
      <Route path="/help" component={HelpPage} />
      <Route component={NotFoundPage} />
    </Switch>
  </BrowserRouter>
);

export default AppRouter;
```

## Redux

- global state
- actual reusability of components
- no more passing props down through multiple components

```jsx
import { createStore } from 'redux';

const store = createStore((state = { count: 0 }) => {
  return state;
});

console.info(store.getState());
```

### Actions and Reducers

- reducers are pure functions!
- never directly change state or action

```jsx
import { createStore } from 'redux';

// action generators
const incrementCount = ({ amount = 1 } = {}) => ({
  type: 'INCREMENT',
  amount,
});

const decrementCount = ({ amount = 1 } = {}) => ({
  type: 'DECREMENT',
  amount,
});

const setCount = ({ amount = 0 } = {}) => ({
  type: 'SET',
  amount,
});

const reset = () => ({
  type: 'RESET',
});

// reducer
const store = createStore((state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return {
        count: state.count + action.amount,
      };
    case 'DECREMENT':
      return {
        count: state.count - action.amount,
      };
    case 'RESET':
      return {
        count: 0,
      };
    case 'SET':
      return {
        count: action.amount,
      };
    default:
      return state;
  }
});

const unsubscribe = store.subscribe(() => {
  console.info(store.getState());
});

store.dispatch(setCount({ amount: 9999 }));
store.dispatch(incrementCount());
store.dispatch(incrementCount({ amount: 101 }));
store.dispatch(decrementCount({ amount: 10 }));
store.dispatch(reset());

unsubscribe();
```

## Higher Order Components

- react component (HOC) that renders another component (normal component)
- reuse code
- render hijacking
- prop manipulation
- abstract state

```jsx
import React from 'react';
import ReactDOM from 'react-dom';

const Info = props => (
  <div>
    <h1>Info</h1>
    <p>the info: {props.info}</p>
  </div>
);

const withAdminWarning = WrappedComponent => {
  return props => (
    <div>
      {props.isAdmin && <p>This is sensitive info!</p>}
      <WrappedComponent {...props} />
    </div>
  );
};

const AdminInfo = withAdminWarning(Info);

ReactDOM.render(
  <AdminInfo isAdmin={true} info="sensitive info here" />,
  document.getElementById('app')
);
```

## Connecting to redux

### Reading

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import AppRouter from './routers/AppRouter';
import configureStore from './store/configureStore';

const store = configureStore();
const jsx = (
  <Provider store={store}>
    <AppRouter />
  </Provider>
);

ReactDOM.render(jsx, document.getElementById('app'));
```

```jsx
import React from 'react';
import { connect } from 'react-redux';

const ExpenseList = props => (
  <div>
    <h1>Expense List</h1>
    {props.filters.text}
    {props.expenses.length}
  </div>
);

const mapStateToProps = state => {
  return {
    expenses: state.expenses,
    filters: state.filters,
  };
};

export default connect(mapStateToProps)(ExpenseList);
```

### Writing

```jsx
import React from 'react';
import { connect } from 'react-redux';
import { setTextFilter } from '../actions/filters';

const ExpenseListFilters = props => (
  <div>
    <input
      type="text"
      value={props.filters.text}
      onChange={e => {
        props.dispatch(setTextFilter(e.target.value));
      }}
    />
  </div>
);

const mapStateToProps = state => {
  return {
    filters: state.filters,
  };
};

export default connect(mapStateToProps)(ExpenseListFilters);
```

## Testing w/ Jest

`add.test.js`

```jsx
const add = (a, b) => a + b;

test('adds two numbers', () => {
  const result = add(3, 4);
  expect(result).toBe(7);
});
```

`yarn test --watchAll`
