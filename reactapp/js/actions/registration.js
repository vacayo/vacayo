import fetch from 'isomorphic-fetch';
import * as types from '../constants/action_types.js';

export function setAddress(address) {
  return {
    type: types.SET_ADDRESS,
    address
  };
}

export function setProperty(property) {
  return {
    type: types.SET_PROPERTY,
    property
  };
}


export function setContact(contact) {
  return {
    type: types.SET_CONTACT,
    contact
  };
}
