import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  // Promise.all to handle promises collectively
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(`Body ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch(error => {
      console.error('Signup system offline');
    });
}
