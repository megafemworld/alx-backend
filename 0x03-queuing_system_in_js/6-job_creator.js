const kue = require('kue');

const queue = kue.createQueue();
const jobData = {
    phoneNumber: String,
    message: String,
};

const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});
