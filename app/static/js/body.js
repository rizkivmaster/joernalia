var CommentBox = React.createClass({displayName: "CommentBox",
  render: function() {
    return (
      React.createElement("div", {className: "commentBox"},
        React.createElement("h1", null, "Comments"),
        React.createElement(CommentList, null),
        React.createElement(CommentForm, null)
      ),
    document.getElementById('example')
    );
  }
});
var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello, world! I am a CommentBox.
      </div>
    );
  }
});
ReactDOM.render(
  <CommentBox />,
  document.getElementById('example')
);