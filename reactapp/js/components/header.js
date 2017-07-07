import React from 'react'
import { Layout } from 'element-react'
import { connect } from 'react-redux'
import logo from '../../../assets/img/vacayo-logo-horiz-white_1.png'


class VacayoHeader extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  render() {
    return (
      <div className="header">
        <Layout.Row gutter="10">
          <Layout.Col xs="8" sm="6" md="4" lg="3"></Layout.Col>
          <Layout.Col xs="4" sm="6" md="8" lg="9">
            <div className="logo">
              <img src={logo} alt="Vacayo: Begin at Home" style={{height: 72}}/>
            </div>
          </Layout.Col>
          <Layout.Col xs="4" sm="6" md="8" lg="9">
            <div className="quote">Quote: $</div>
          </Layout.Col>
          <Layout.Col xs="8" sm="6" md="4" lg="3"></Layout.Col>
        </Layout.Row>
      </div>
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

export default connect(mapStateToProps, mapDispatchToProps)(VacayoHeader);