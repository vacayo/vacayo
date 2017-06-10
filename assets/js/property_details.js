import React from 'react';
import { Button, Card, Row, Col, Input } from 'react-materialize';

class PropertyDetails extends React.Component {
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
          <Input s={12} label="Address" />
        </Row>
        <Row>
          <Input s={12} label="Address 2" />
        </Row>
        <Row>
          <Input s={4} label="City" />
          <Input s={4} label="State" />
          <Input s={4} label="Zip Code" />
        </Row>
        <Row>
          <Input s={4} label="Bedrooms" />
          <Input s={4} label="Bathrooms" />
          <Input s={4} label="Size (square feet)" />
        </Row>
        <Row>
          <Input s={6} label="Has Rented Before?" />
          <Input s={6} label="Available Date" />
        </Row>
      </Card>
    )
  }
}

export default PropertyDetails;