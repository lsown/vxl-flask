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
    this.state = { field:""}
    }
    render() {
      return (
        ("input", {type:"text", id:"name", name:"name", size:"10" })
      );
    }
  }

  class inputLabel extends React.Component {
    constructor(props) {
    super(props);
    this.state = {}
    }
    
    render() {
      return (
        ("label", { htmlFor:"inputField", className:"test test2 test3"}, "Input field: ")
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
      e(NewLikeButton, { commentID: commentID }),
      domContainer
    );
  });
  
ReactDOM.render(
  e(inputLabel, null, e(inputText, null)), 
  document.querySelector('.panel4')
)


ReactDOM.render(
  e(inputText), 
  document.querySelector('.panel3')
)
