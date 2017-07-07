import React from 'react';
import fetch from 'isomorphic-fetch';
import AutoComplete from 'material-ui/AutoComplete';
import RaisedButton from 'material-ui/RaisedButton';
import {Grid, Row, Col} from 'react-flexbox-grid';
import {setAddress} from '../actions/registration.js'
import {connect} from 'react-redux'


class AddressSearch extends React.Component {
  constructor(props) {
    super(props);
    this.searchAPI = '/api/address?query=';
    this.state = {
      dataSource : [],
      searchText : props.address
    }
  }

  search() {
    const self = this;
    const url  = this.searchAPI + this.state.searchText;
    if(this.state.searchText !== '') {
      fetch(url)
        .then(
          response => response.json(),
          error => console.log('An error occurred while looking up address:', error)
        )
        .then(
          json => self.setState({dataSource: json.results})
        )
    }
  }

  onUpdateInput = (searchText) => {
    this.setState({
      searchText: searchText
    }, this.search);
  };

  onNewRequest = (address, index) => {
    this.props.onSetAddress(address);
    this.onNext();
  };

  onNext = (object) => {
    this.props.onNext(this.props.stepIndex)
  };

  render() {
    return (
      <Grid fluid>
        <Row>
          <Col xs={9}>
            <AutoComplete
              hintText="Address"
              searchText={this.state.searchText}
              onUpdateInput={this.onUpdateInput}
              onNewRequest={this.onNewRequest}
              dataSource={this.state.dataSource}
              filter={(searchText, key) => true}
              fullWidth={true}
            />
          </Col>
          <Col xs={3}>
            <RaisedButton
              label="Get Quote"
              primary={true}
              onTouchTap={this.onNext}
              fullWidth={true}
            />
          </Col>
        </Row>
      </Grid>
    );
  }
}

const mapStateToProps = state => {
  return {
    address : state.address
  }
};

const mapDispatchToProps = dispatch => {
  return {
    onSetAddress : address => {
      dispatch(setAddress(address))
    }
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(AddressSearch);
