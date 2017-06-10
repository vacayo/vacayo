import React from 'react';
import AutoComplete from 'material-ui/AutoComplete';

class AddressSearch extends React.Component {
  constructor(props) {
    super(props);
    this.searchAPI = '/api/address?query=';
    this.state = {
      dataSource : [],
      searchText : ''
    }
  }

  search() {
    const self = this;
    const url  = this.searchAPI + this.state.searchText;
    if(this.state.searchText !== '') {
      fetch(url).then(function(response) {
        if (response.status >= 400) {
          throw new Error("Bad response from server");
        }
        return response.json()
      }).then(function(response) {
        console.log(response.results);
        self.setState({
          dataSource: response.results
        });
      })
    }
  }

  onUpdateInput = (searchText) => {
    this.setState({
      searchText: searchText
    }, this.search);
  };

  onNewRequest = () => {
    //this.setState({
    //  searchText: ''
    //});
  };

  render() {
    return (
      <div>
        <AutoComplete
          hintText="Address"
          searchText={this.state.searchText}
          onUpdateInput={this.onUpdateInput}
          onNewRequest={this.onNewRequest}
          dataSource={this.state.dataSource}
          filter={(searchText, key) => true}
        />
      </div>
    );
  }
}

export default AddressSearch;