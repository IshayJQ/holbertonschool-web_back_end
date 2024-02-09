import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  // Promise.all to handle promises collectively
  Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch(() => new Error());
}
