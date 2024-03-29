'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked comment number ' + this.props.commentID;
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

class NewLikeButton extends React.Component {
    constructor(props) {
      super(props);
      this.state = { liked: false };
    }
  
    render() {
      if (this.state.liked) {
        return e(
            'button', 
            { onClick: () => this.setState({ liked: false})},
        'Unlike'
        );
      } else {
        return e(
          'button',
          { onClick: () => this.setState({ liked: true }) },
          'Like'
        );
      }
    }
  }

  class inputText extends React.Component {
    constructor(props) {
    super(props);
    this.state = { name: this.props.name, value: this.props.value}
    }
    render() {
      return (
        e("input", {type:"text", id:"name", name:this.props.name, size:"10", placeholder:"Empty" })
      );
    }
  }

  class inputLabel extends React.Component {
    constructor(props) {
    super(props);

    }
    
    render() {
      return (
        e("label", { htmlFor:"inputField", className:"test test2 test3"}, "Input field: ")
        );
    }
  }

/*
  function Example() {
    // Declare a new state variable, which we'll call "count"  const 
    [count, setCount] = useState(0);
    return (
      <div>
        <p>You clicked {count} times</p>
        <button onClick={() => setCount(count + 1)}>
          Click me
        </button>
      </div>
    );
  }*/

// Find all DOM containers, and render Like buttons into them.
document.querySelectorAll('.like_button_container')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    const commentID = parseInt(domContainer.dataset.commentid, 10);
    ReactDOM.render(
      e(LikeButton, { commentID: commentID }),
      domContainer
    );
  });

  document.querySelectorAll('.new_like_button_container')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    const commentID = parseInt(domContainer.dataset.commentid, 10);
    ReactDOM.render(
      e(NewLikeButton, { commentID: commentID, id: "hello" }),
      domContainer
    );
  });
  
ReactDOM.render(e(inputLabel), document.querySelector('.renderInput'));

ReactDOM.render(e(inputText, { name: "rawr"}, null), document.querySelector('.renderText'));

/* https://reactgo.com/react-createelement-example/ */