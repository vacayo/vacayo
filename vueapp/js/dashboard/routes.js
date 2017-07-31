import App from './App'
import Properties from './views/Properties'
import Maintenance from './views/Maintenance'

export default [
  {
    path: '/',
    name: 'Dashboard',
    redirect: 'properties',
    component: App,
    children: [
      {
        path: 'properties',
        name: 'Properties',
        component: Properties
      },
      {
        path: 'maintenance',
        name: 'Maintenance',
        component: Maintenance
      }
    ]
  }
]
