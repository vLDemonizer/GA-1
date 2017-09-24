class Option extends React.Component {
  render() {
    let product = this.props.product;
    return (
      <option>
        {product}
      </option>
    );
  }
}

function showModal(move) {
  var moveOut = parseInt(move)

  $.ajax({
    url: '/reporte/ajax/get_move_out_detail/',
    data: {
      'move_out_pk': moveOut,
    },
    dataType: 'json',
    success: (data) => {
      var products = data['products']
      var product_list = [];
      for (var i = 0; i < data['products'].length; i++) {
        product_list.push(<Option product={ data['products'][i][0] }/>);
      }

      const selectStyle = {
        width: "350px",
        height: "500px",
        marginBottom: "1rem",
      };
      ReactDOM.render(
        <div className="container-fluid">
          <div className="row">
            <div className="col">
              <label className="row"><strong> From </strong></label>
              <input
                className="row form-control"
                type="text"
                placeholder={ data['origin'] }
                readOnly/>
            </div>
            <div className="col">
              <label className="row"><strong> To </strong></label>
              <input
                className="row form-control"
                type="text"
                placeholder={ data['destiny'] }
                readOnly
                style={{ marginBottom: "1rem" }}/>
            </div>
          </div>
          <div className="row">
            <div className="col">
              <label className="row"><strong> Product Description </strong></label>
              <label className="row"> { data['product_class'] } </label>
            </div>
            <div className="col">
              <label className="row"><strong> Amount </strong></label>
              <input
                style={{ width: "130px" }}
                className="row form-control"
                type="number"
                value={ data['products'].length }
                readOnly
                style={{ marginBottom: "1rem" }}/>
            </div>
          </div>
          <div className="row">
            <div className="col">
              <label className="row"><strong> Products Codes </strong></label>
              <select
                className="row"
                readOnly
                multiple="multiple"
                >
                  { product_list }
              </select>
            </div>
            <div className="col">
              <label className="row"><strong> Authorized By </strong></label>
              <input
                className="row form-control"
                type="text"
                placeholder={ data['authorized_by'] }
                readOnly
                style={{ marginBottom: "1rem" }}/>
                <label className="row"><strong> Received By </strong></label>
                <input
                  className="row form-control"
                  type="text"
                  placeholder={ data['received_by'] }
                  readOnly
                  style={{ marginBottom: "1rem" }}/>
                <label className="row"><strong> Dispatched By </strong></label>
                <input
                  className="row form-control"
                  type="text"
                  placeholder={ data['given_by'] }
                  readOnly/>
            </div>
          </div>
        </div>,
        document.getElementById('id_modal_body')
      );
    }
  });

  $('#id_modal_move').modal('show');
}
