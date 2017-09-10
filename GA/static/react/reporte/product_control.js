class Option extends React.Component {
    render () {
        let product = this.props.product.fields;
        let product_pk = this.props.product.pk;
        return (
            <option
                name={product_pk}
                >{product.name} - {product.product_type} - {product.size} - {product.brand} - {product.department}
            </option>
        );
    }
}

class HiddenInput extends React.Component {
  render () {
    let name = this.props.name;
    return (
      <input
        type="hidden"
        id={"id_" + name}
        name={name}
        value={this.props.primary_key}
        required
      />
    );
  }
}

class ProductList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          key: 0,
          name: '',
          type: '',
          brand: '',
          size: '',
          department: '',
          description: '',
          is_disposable: false,
          min_amount: '',
          cost_value: '',
          our_value: '',
          their_value: '',

        };
        this.handleSelection = this.handleSelection.bind(this);
        this.changeState = this.changeState.bind(this);
    }

    changeState(e) {
      console.log(this.state.is_disposable)
      this.setState({is_disposable: !this.state.is_disposable})
    }

    handleSelection(e) {
        let options = e.target.list.options
        let productText = $("#product_info").val();
        for(var i = 0; i < options.length; i++) {
          if (options[i].innerText === productText) {
            let product = this.props.products[i];
            this.setState({
              key: product.pk,
              name: product.fields.name,
              type: product.fields.product_type,
              brand: product.fields.brand,
              size: product.fields.size,
              department: product.fields.department,
            });
          }
        }
    }

    render () {
        let products = this.props.products;
        var product_list = [];
        for (var i = 0; i < products.length; i++) {
            product_list.push(<Option product={products[i]} key={'a' + i}/>);
        }
        return (
          <div className="container-fluid">
            <label>Search Product</label>
            <input
              onInput={this.handleSelection}
              id="product_info"
              className="form-control"
              type="text"
              list="product_options"
              autoComplete="off"
            />
            <datalist id="product_options">
              {product_list}
            </datalist>
            <HiddenInput primary_key={this.state.key} name={"product_class"}/>
          </div>
        );
    }
}
