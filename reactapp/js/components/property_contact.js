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
import {setProperty} from '../actions/registration.js'
import {connect} from 'react-redux'


class PropertyContact extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      contact: props.contact
    }
  }

  onPrev = (object) => {
    this.props.onPrev(this.props.stepIndex)
  };

  onNext = (object) => {
    this.props.onNext(this.props.stepIndex)
  };

  render() {
    const {contact} = this.state;

    return (
      <Grid fluid>
        <Row>
          <Col xs={6}>
            <TextField
              floatingLabelText="First Name"
              fullWidth={true}
              required={true}
            />
          </Col>
          <Col xs={6}>
            <TextField
              floatingLabelText="Last Name"
              fullWidth={true}
              required={true}
            />
          </Col>
        </Row>
        <Row>
          <Col xs={6}>
            <TextField
              floatingLabelText="Email"
              fullWidth={true}
              required={true}
            />
          </Col>
          <Col xs={6}>
            <TextField
              floatingLabelText="Phone Number"
              fullWidth={true}
              required={true}
            />
          </Col>
        </Row>
        <Row between="xs">
          <FlatButton
            label="Back"
            primary={true}
            onTouchTap={this.onPrev}
          />
          <RaisedButton
            label="Done!"
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
    contact : state.contact
  }
};

const mapDispatchToProps = dispatch => {
  return {
    onSetContact : contact => {
      dispatch(onSetContact(contact))
    }
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(PropertyContact);
