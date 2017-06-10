import React from 'react';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';
import AddressSearch from './property_address.js'
import PropertyDetails from './property_details.js'
import PropertyContact from './property_contact.js'
import {
  Step,
  Stepper,
  StepLabel,
  StepContent,
} from 'material-ui/Stepper';

class RegistrationFlow extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      finished: false,
      stepIndex: 0
    }
  }

  handleNext = () => {
    const {stepIndex} = this.state;
    this.setState({
      stepIndex: stepIndex + 1,
      finished: stepIndex >= 3
    });
  };

  handlePrev = () => {
    const {stepIndex} = this.state;
    if (stepIndex > 0) {
      this.setState({stepIndex: stepIndex - 1});
    }
  };

  renderStepActions(stepIndex) {
    return (
      <div>
        {stepIndex <= 3 && (
        <RaisedButton
          label={stepIndex === 3 ? 'Finish' : 'Next'}
          disableTouchRipple={true}
          disableFocusRipple={true}
          primary={true}
          onTouchTap={this.handleNext}
          style={{marginRight: 12}}
        />
        )}
        {stepIndex > 0 && (
          <FlatButton
            label="Back"
            disabled={stepIndex === 0}
            disableTouchRipple={true}
            disableFocusRipple={true}
            onTouchTap={this.handlePrev}
          />
        )}
      </div>
    );
  }

  renderStepContent(stepIndex) {
    switch (stepIndex) {
      case 0:
        return (<AddressSearch />);
      case 1:
        return (<PropertyDetails />);
      case 2:
        return 'This is the bit I really care about! $$$';
      case 3:
        return (<PropertyContact />);
      default:
        return 'Done!';
    }
  }

  render() {
    const {finished, stepIndex} = this.state;
    const contentStyle = {margin: '0 16px'};

    return (
      <div style={{width: '100%', maxWidth: 700, margin: 'auto'}}>
        <Stepper activeStep={stepIndex}>
          <Step>
            <StepLabel>Property Address</StepLabel>
          </Step>
          <Step>
            <StepLabel>Property Details</StepLabel>
          </Step>
          <Step>
            <StepLabel>Quote</StepLabel>
          </Step>
          <Step>
            <StepLabel>Contact Info</StepLabel>
          </Step>
        </Stepper>
        <div style={contentStyle}>
          <div>{this.renderStepContent(stepIndex)}</div>
          <div>{this.renderStepActions(stepIndex)}</div>
        </div>
      </div>
    );
  }
}

export default RegistrationFlow;