import 'babel-polyfill'
import React from 'react'
import ReactDOM from 'react-dom'
import thunkMiddleware from 'redux-thunk'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import { createStore, combineReducers, applyMiddleware } from 'redux'
import { createLogger } from 'redux-logger'
import { Provider } from 'react-redux'
import * as registrationApp from './reducers/registration.js'
import RegistrationFlow from './components/registrationflow.js'
import VacayoHeader from './components/header.js'

// Needed for onTouchTap http://stackoverflow.com/a/34015469/988941
import injectTapEventPlugin from 'react-tap-event-plugin'
injectTapEventPlugin();

// Needed to set default locale to English for Element-React
import 'element-theme-default';
import { i18n } from 'element-react'
import locale from 'element-react/src/locale/lang/en'
i18n.use(locale);

//This is the store we create with redux's createStore method
const loggerMiddleware = createLogger();
const reducer = combineReducers(registrationApp);
const store = createStore(reducer, applyMiddleware(thunkMiddleware, loggerMiddleware));

class App extends React.Component {
    render() {
        return (
            <MuiThemeProvider>
              <div>
                <VacayoHeader />
                <RegistrationFlow />
              </div>
            </MuiThemeProvider>
        )
    }
}

ReactDOM.render(<Provider store={store}><App /></Provider>, document.getElementById('container'));

//style={{background: '#424242'}}