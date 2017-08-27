class Name extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  100,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }
  render () {
    return (
      <div className="form-group">
        <label>Name <small className="text-form text-muted">Character limit {this.state.current} of 100.</small></label>
        <input
          type="text"
          className="form-control"
          placeholder="Enter product name"
          value={this.state.value}
          onChange={this.handleChange}
        />
        <small className="form-text text-muted">Remember to double check the information you are submitting</small>
      </div>
    );
  }
};

class Brand extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  30,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }
  render () {
    return (
      <div className="form-group">
        <label>Brand <small className="text-form text-muted">Character limit {this.state.current} of 30.</small></label>
        <input
          type="text"
          className="form-control"
          placeholder="Enter brand name"
          value={this.state.value}
          onChange={this.handleChange}
        />
      </div>
    );
  }
};

class Department extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  50,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }
  render () {
    return (
      <div className="form-group">
        <label>Department <small className="text-form text-muted">Character limit {this.state.current} of 50.</small></label>
        <input
          type="text"
          className="form-control"
          placeholder="Enter product's department"
          value={this.state.value}
          onChange={this.handleChange}
        />
      </div>
    );
  }
};

class Size extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  15,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
      console.log('inhere');
  }

  render () {
    return (
      <div className="form-group">
        <label>Size <small className="text-form text-muted">Character limit {this.state.current} of 15.</small></label>
        <input
          type="text"
          className="form-control"
          placeholder="Enter product's size name"
          value={this.state.value}
          onChange={this.handleChange}
        />
      </div>
    );
  }
};

class Description extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      limit:  120,
      current: 0,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    var current = event.target.value.length;
    if (!(current > this.state.limit))
      this.setState({
        value: event.target.value,
        current: current
      });
  }

  render () {
    return (
      <div className="form-group">
        <label>Description <small className="text-form text-muted">Character limit {this.state.current} of 120.</small></label>
        <textarea
          type="text"
          className="form-control"
          placeholder="Enter product's description name"
          rows="3"
          value={this.state.value}
          onChange={this.handleChange}>
        </textarea>
      </div>
    );
  }
};

class ProductForm extends React.Component {
  render () {
    return (
      <div className="container-fluid">
        <div className="text-center">
          <h1 className="display-3">Create Product</h1>
        </div>
        <Name />
        <Brand />
        <Department />
        <Size />
        <Description />
        <div className="text-center">
          <button className="btn btn-primary btn-lg">Submit</button>
        </div>
        </div>
    );
  }
};

ReactDOM.render (
  <ProductForm />,
  document.getElementById('root')
);
