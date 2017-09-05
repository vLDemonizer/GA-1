class InOut extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      selectedOption: 'option1'
    };

    this.handleOptionChange = this.handleOptionChange.bind(this);
  }


  handleOptionChange(evt){
      this.setState({
        selectedOption: evt.target.value
      });
  }

  render (){
    return (
      <div className="btn-group form-control text-center" data-toggle="buttons">
        <label className="btn btn-primary btn-lg">
          <input id="option1" type="radio" value="option1"
            checked={this.state.selectedOption === 'option1'}
            onChange={this.handleOptionChange} />
          Entrada
        </label>
        <label className="btn btn-primary btn-lg">
          <input id="option2" type="radio" value="option2"
            checked={this.state.selectedOption === 'option2'}
            onChange={this.handleOptionChange} />
            Salida
        </label>
      </div>
    );
  }
};

ReactDOM.render(
  <InOut />,
  document.getElementById('root')
);
