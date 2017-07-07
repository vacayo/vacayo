import * as types from '../constants/action_types.js';

const default_address = '';
export function address(state = default_address, action) {
  switch (action.type) {
    case types.SET_ADDRESS:
      return action.address;

    default:
      return state;
  }
}


const default_property = {
  bedrooms: '',
  bathrooms: '',
  home_type: '',
  home_size: ''
};
export function property(state = default_property, action) {
  switch (action.type) {
    case types.SET_PROPERTY:
      return Object.assign({}, state, action.property);

    default:
      return state;
  }
}


const default_contact = {
  first_name: '',
  last_name: '',
  phone: '',
  email: ''
};
export function contact(state = default_contact, action) {
  switch (action.type) {
    case types.SET_CONTACT:
      return Object.assign({}, state, action.contact);

    default:
      return state;
  }
}