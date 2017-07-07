import React from 'react';
import TextField from 'material-ui/TextField'
import SelectField from 'material-ui/SelectField';
import MenuItem from 'material-ui/MenuItem';
import Checkbox from 'material-ui/Checkbox';
import DatePicker from 'material-ui/DatePicker';
import NumberInput from 'material-ui-number-input';
import RaisedButton from 'material-ui/RaisedButton';
import FlatButton from 'material-ui/FlatButton';
import {Grid, Row, Col} from 'react-flexbox-grid';
import {setProperty} from '../actions/registration.js';
import {connect} from 'react-redux';
var MediaQuery = require('react-responsive');


class PropertyDetails extends React.Component {
  constructor(props) {
    super(props);
    this.searchAPI = '/api/property?address=';
    this.state = {
      address: props.address,
      bedrooms: props.bedrooms,
      bathrooms: props.bathrooms,
      home_type: props.home_type,
      home_size: props.home_size,
      has_rented: false
    }
  }

  onPrev = (object) => {
    this.props.onPrev(this.props.stepIndex)
  };

  onNext = (object) => {
    this.props.onNext(this.props.stepIndex)
  };

  onBedroomsChange = (event, key, payload) => {
    this.setState({bedrooms: payload});
  };

  onBathroomsChange = (event, key, payload) => {
    console.log(payload);
    this.setState({bathrooms: payload});
  };

  onTypeChange = (event, key, payload) => {
    this.setState({home_type: payload});
  };

  onSizeChange = (event) => {
    this.setState({home_size: event.target.value});
  };

  onHasRented = (event, isInputChecked) => {
    this.setState({has_rented: isInputChecked});
  };

  componentDidMount = () => {
    this.search()
  };

  search = () => {
    const self = this;
    const url  = this.searchAPI + this.state.address;
    if(this.state.address !== '') {
      fetch(url)
        .then(
          response => response.json(),
          error => console.log('An error occurred while fetching property:', error)
        )
        .then(
          json => {
            let props = json.results;
            self.props.onSetProperty(props);
            self.setState({
              address: props.address,
              bedrooms: props.bedrooms,
              bathrooms: props.bathrooms,
              home_type: props.home_type,
              home_size: props.home_size,
            });
          }
        )
    }
  };

  render() {
    return (
      <Grid fluid>
        <Row between="xs">
          <Col xs={6}>
            <SelectField
              floatingLabelText="Bedrooms"
              fullWidth={true}
              required={true}
              value={this.state.bedrooms}
              onChange={this.onBedroomsChange}
            >
              <MenuItem value={0} primaryText="Studio" />
              <MenuItem value={1} primaryText="1 Bedroom" />
              <MenuItem value={2} primaryText="2 Bedrooms" />
              <MenuItem value={3} primaryText="3 Bedrooms" />
              <MenuItem value={4} primaryText="4 Bedrooms" />
              <MenuItem value={5} primaryText="5 Bedrooms" />
              <MenuItem value={6} primaryText="6 Bedrooms" />
              <MenuItem value={7} primaryText="7+ Bedrooms" />
            </SelectField>
          </Col>
          <Col xs={6}>
            <SelectField
              floatingLabelText="Bathrooms"
              fullWidth={true}
              required={true}
              value={this.state.bathrooms}
              onChange={this.onBathroomsChange}
            >
              <MenuItem value={1.0} primaryText="1 Bathoom" />
              <MenuItem value={1.5} primaryText="1.5 Bathooms" />
              <MenuItem value={2} primaryText="2 Bathooms" />
              <MenuItem value={2.5} primaryText="2.5 Bathooms" />
              <MenuItem value={3} primaryText="3 Bathooms" />
              <MenuItem value={3.5} primaryText="3.5 Bathooms" />
              <MenuItem value={4} primaryText="4+ Bathooms" />
            </SelectField>
          </Col>
        </Row>
        <Row between="xs">
          <Col xs={6}>
            <SelectField
              floatingLabelText="Type"
              fullWidth={true}
              required={true}
              value={this.state.home_type}
              onChange={this.onTypeChange}
            >
              <MenuItem value="SingleFamily" primaryText="Single Family" />
              <MenuItem value="Duplex" primaryText="Duplex" />
              <MenuItem value="Triplex" primaryText="Triplex" />
              <MenuItem value="Quadruplex" primaryText="Quadruplex" />
              <MenuItem value="Condominium" primaryText="Condominium" />
              <MenuItem value="Cooperative" primaryText="Cooperative" />
              <MenuItem value="Mobile" primaryText="Mobile" />
              <MenuItem value="Apartment" primaryText="Apartment" />
              <MenuItem value="Timeshare" primaryText="Timeshare" />
            </SelectField>
          </Col>
          <Col xs={6}>
            <NumberInput
              floatingLabelText="Size (square feet)"
              strategy="ignore"
              fullWidth={true}
              required={true}
              min={100}
              value={this.state.home_size}
              onChange={this.onSizeChange}
            />
          </Col>
        </Row>
        <Row between="xs" bottom="xs">
          <Col xs={6}>
            <Checkbox
              label="Has this property been rented before?"
              labelPosition="right"
              onCheck={this.onHasRented}
              style={{paddingTop:38, paddingBottom:10}}
            />
          </Col>
          <Col xs={6}>
            {this.state.has_rented && (
            <NumberInput
              floatingLabelText="Last Rent Amount (USD)?"
              disabled={!this.state.has_rented}
              strategy="ignore"
              fullWidth={true}
              required={true}
              min={100}
              />
          )}
          </Col>
        </Row>
        <Row between="xs">
          <MediaQuery orientation='landscape'>
            {(matches) => {
              return <DatePicker
                floatingLabelText="Available Date"
                fullWidth={true}
                required={true}
                autoOk={true}
                mode={(matches) ? 'landscape' : 'portrait'}
                locale="en-US"
                firstDayOfWeek={0}
              />
            }}
          </MediaQuery>
        </Row>
        <Row between="xs">
          <FlatButton
            label="Back"
            primary={true}
            onTouchTap={this.onPrev}
          />
          <RaisedButton
            label="Next"
            primary={true}
            onTouchTap={this.onNext}
          />
        </Row>
      </Grid>
    )
  }
}

const mapStateToProps = state => {
  return {
    address : state.address,
    bedrooms: state.property.bedrooms,
    bathrooms: state.property.bathrooms,
    home_type: state.property.home_type,
    home_size: state.property.home_size
  }
};

const mapDispatchToProps = dispatch => {
  return {
    onSetProperty : property => {
      dispatch(setProperty(property))
    }
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(PropertyDetails);
