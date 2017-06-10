import React from 'react';
import { Button, Card, Row, Col, Input } from 'react-materialize';

class PropertyContact extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    }
  }

  render() {
    const {finished, stepIndex} = this.state;
    const contentStyle = {margin: '0 16px'};

    return (
      <Card>
        <Row>
          <Input s={6} label="First Name" />
          <Input s={6} label="Last Name" />
        </Row>
        <Row>
          <Input s={12} label="Email" />
        </Row>
        <Row>
          <Input s={6} label="Phone" />
        </Row>
      </Card>
    )
  }
}

export default PropertyContact;