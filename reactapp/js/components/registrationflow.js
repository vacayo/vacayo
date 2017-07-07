import React from 'react'
//import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card'
//import AddressSearch from './property_address.js'
//import PropertyDetails from './property_details.js'
//import PropertyContact from './property_contact.js'

import { Steps } from 'element-react'
import { connect } from 'react-redux'


class Stepper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stepIndex: 0
    }
  }

  render() {
    const {stepIndex} = this.state;

    return (
      <Steps active={stepIndex} finishStatus="success">
        <Steps.Step title="Step 1" description="Property Address"></Steps.Step>
        <Steps.Step title="Step 2" description="Property Details"></Steps.Step>
        <Steps.Step title="Step 3" description="Contact Info"></Steps.Step>
      </Steps>
    );
  }
}

class RegistrationFlow extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stepIndex: 0
    }
  }

  onNext = (stepIndex) => {
    this.setState({
      stepIndex: stepIndex + 1,
    });
  };

  onPrev = (stepIndex) => {
    if (stepIndex > 0) {
      this.setState({stepIndex: stepIndex - 1});
    }
  };

  renderStepContent(stepIndex) {
    switch (stepIndex) {
      case 0:
        return (<AddressSearch onNext={this.onNext} onPrev={this.onPrev} stepIndex={0} />);
      case 1:
        return (<PropertyDetails onNext={this.onNext} onPrev={this.onPrev} stepIndex={1} />);
      case 2:
        return (<PropertyContact onNext={this.onNext} onPrev={this.onPrev} stepIndex={2} />);
      default:
        return 'Done!';
    }
  }

  render() {
    const {stepIndex} = this.state;

    return (
      <Card style={{width: '100%', maxWidth: 800, margin: 'auto'}}>
        <Stepper />
        <CardText>
          {this.renderStepContent(stepIndex)}
        </CardText>
      </Card>
    );
  }
}

const mapStateToProps = state => {
  return {
  }
};

const mapDispatchToProps = dispatch => {
  return {
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(RegistrationFlow);