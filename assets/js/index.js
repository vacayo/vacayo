import React from 'react';
import ReactDOM from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RegistrationFlow from './registrationflow.js'

// Needed for onTouchTap http://stackoverflow.com/a/34015469/988941
import injectTapEventPlugin from 'react-tap-event-plugin';
injectTapEventPlugin();

// polyfills for fetch
require('es6-promise').polyfill();
require('isomorphic-fetch');

class App extends React.Component {
    render() {
        return (
            <MuiThemeProvider>
              <div>
                <RegistrationFlow />

              </div>
            </MuiThemeProvider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('container'));