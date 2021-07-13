import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518782',
    message: 'This is the code 1232 to verify your account'
  }
];

describe('createPushNotificationsJobs', function() {


    before(() => queue.testMode.enter());
    afterEach(() => queue.testMode.clear());
    after(() => queue.testMode.exit());


    it('display a error message if jobs is not an array', () => {
        expect(
	  ()=>createPushNotificationsJobs({
          phoneNumber: '123',
          message: 'abc'}, queue)
	).to.throw('Jobs is not an array')
    });

    it('create two new jobs to the queue', () => {
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs.[0].data.phoneNumber).to.equal('4153518780');
        expect(queue.testMode.jobs.[1].data.phoneNumber).to.equal('4153518782');
    });
});
