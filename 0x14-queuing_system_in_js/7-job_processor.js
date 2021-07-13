import kue from 'kue';

const queue = kue.createQueue();
const bl = ['4153518780', '4153518781']

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100, job.data);
  if (bl.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100, job.data);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    )
    done();
  }
}

queue.process('push_notification_code_2', '2',(job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
})
