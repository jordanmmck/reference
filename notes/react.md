# React

## useState

Allows using state in a stateless functional component.

```js
const [title, setTitle] = useState("");
setTitle("");
```

## useEffect

```js
// runs once when component mounts
useEffect(() => {}, []);

// runs only when `notes` changes
useEffect(() => {}, [notes]);

// runs when component mounts
// returned function runs when component unmount
useEffect(() => {
  console.log("setting up...");
  return () => {
    console.log("cleaning...");
  };
}, []);
```

## useReducer

If the state management gets more complex you can use a reducer to pull that logic out of your component.

```js
const notesReducer = (state, action) => {
  switch (action.type) {
    case "POPULATE_NOTES":
      return action.notes;
    case "ADD_NOTE":
      return [...state, { title: action.title, body: action.body }];
    case "REMOVE_NOTE":
      return state.filter((note) => note.title !== action.title);
    default:
      return state;
  }
};

const [notes, dispatch] = useReducer(notesReducer, []);
dispatch({ type: "POPULATE_NOTES", notes });
dispatch({ type: "ADD_NOTE", title, body });
dispatch({ type: "REMOVE_NOTE", title });
```

## useContext

Basically allows you to pass data/functions to a whole bunch of components, as well as their children etc. Basically make some stuff available to all of them easily.
