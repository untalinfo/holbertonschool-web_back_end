import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  const signIn = await signUpUser(firstName, lastName)
    .then((response) => ({
      status: 'fulfilled',
      value: response,
    }))
    .catch((e) => ({
      status: 'rejected',
      value: e.toString(),
    }));
  const upload = await uploadPhoto(fileName)
    .catch((e) => ({
      status: 'rejected',
      value: e.toString(),
    }));

  return [signIn, upload];
}

export default handleProfileSignup;
