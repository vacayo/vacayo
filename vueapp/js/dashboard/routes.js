import App from './App'
import Login from './views/Login'
import Signup from './views/Signup'

export default [
  {
    path: '/',
    name: 'Dashboard',
    component: App,
    children: [
      {
        path: 'login',
        name: 'Log In',
        component: Login
      },
      {
        path: 'signup',
        name: 'Sign Up',
        component: Signup
      }
    ]
  }
]
