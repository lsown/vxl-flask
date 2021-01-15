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

  class voxaTextField extends React.Component {
    constructor(props) {
      super(props);
      this.state = { field: "" };
    }

    setFieldValue = event => {
      this.setState({field: event.target.value});
    };

    render() {
      <p>Hello</p>
    }
  }



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

  
ReactDOM.render(voxaTextField, document.querySelector('.counter_button'));