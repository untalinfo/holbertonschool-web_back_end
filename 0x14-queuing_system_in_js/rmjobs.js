import kue from 'kue';

const queue = kue.createQueue();

// config
const eList = [
  'enqueue', 'start', 'promotion',
  'progress', 'failed attempt',
  'failed', 'complete', 'remove'
  ];
const sList = ['active', 'inactive', 'complete', 'failed']
const from = 0;
const to = 3;
const typeJob = 'push_notification_code';
const typeStatus = sList[2];
const orderList = ['asc', 'dsc'];
const order = orderList[0]

queue.inactiveCount( function( err, total ) { 
  console.log(`Total inactive: ${total}`);
  if( total > 100000 ) {
    console.log( 'We need some back pressure here' );
  }
});

queue.activeCount( function( err, total ) {
  console.log(`Total active: ${total}`);
  if( total > 100000 ) {
    console.log( 'We need some back pressure here' );
  }
});

queue.completeCount( function( err, total ) {
  console.log(`Total completed: ${total}`);
  if( total > 100000 ) {
    console.log( 'wow' );
  }
});


queue.failedCount( function( err, total ) {
  console.log(`Total failed: ${total}`);
  if( total > 100000 ) {
    console.log( 'We need some back pressure here' );
  }
});

queue.delayedCount( function( err, total ) {
  console.log(`Total delayed: ${total}`);
  if( total > 100000 ) {
    console.log( 'We need some back pressure here' );
  }
});


queue.active( function( err, ids ) {
  console.log('active ids');
  console.log(ids);
  // you may want to fetch each id to get the Job object out of it...
});

queue.inactive( function( err, ids ) {
  console.log('inactive ids');
  console.log(ids);
});

queue.complete( function( err, ids ) {
  console.log('completed ids');
  console.log(ids);
});

queue.failed( function( err, ids ) {
  console.log('failed ids');
  console.log(ids);
});

queue.delayed( function( err, ids ) {
  console.log('delayed ids');
  console.log(ids);
});

console.log(`
type of job: ${ typeJob },
type of Status: ${ typeStatus }
range: ${ from } - ${ to }
order: ${ order }
`)
kue.Job.rangeByType( typeJob, typeStatus, from, to, order, function( err, jobs ) {
  if (jobs.length == 0) console.log('no data to delete, change parameters');
  jobs.forEach((j) => {
      j.remove(function(err){
        if (err) throw err;
        console.log('removed completed job #%d', j.id);
      });

  });
});

