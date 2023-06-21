const { Telegraf } = require('telegraf');
const { MongoClient } = require('mongodb');
const moment = require('moment-timezone');

const bot = new Telegraf('5166769555:AAGEVsxFuRxUjiFmBxrtjZ7qjv2SeZYRp_s');

const dbClient = new MongoClient('mongodb+srv://RPN:RPN@tgreporternew.rys1amm.mongodb.net/', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

async function connectToDatabase() {
  await dbClient.connect();
  const db = dbClient.db('my_db');
  return db.collection('reports');
}

bot.start((ctx) => ctx.reply('Bot started'));

bot.on('text', async (ctx) => {
  const messageText = ctx.message.text;
  if (messageText.startsWith('@admin')) {
    const loadingMessage = await ctx.reply('Report sending ○○○○○○○○○');

    const reportText = messageText.slice(6);

    const indiaTimezone = 'Asia/Kolkata';
    const nowInIndia = moment().tz(indiaTimezone);
    const reportTime = nowInIndia.format('hh:mm:ss A');
    const reportDate = nowInIndia.format('DD-MM-YYYY');
    const reportDay = nowInIndia.format('dddd');

    const trackId = `#MB${Math.floor(Math.random() * 1000000)}`;
    const reportTop = '✅ Rᴇᴘᴏʀᴛ sᴇɴᴅ ᴛᴏ ᴀᴅᴍɪɴ ✅';

    const report = {
      reportTop,
      reporter: ctx.from.first_name,
      reporterId: ctx.from.id,
      trackId,
      reportText,
      reportTime,
      reportDate,
      reportDay,
    };

    const collection = await connectToDatabase();
    await collection.insertOne(report);

    for (let i = 0; i < 10; i++) {
      const filled = '●'.repeat(i + 1);
      const unfilled = '○'.repeat(10 - (i + 1));
      const loadingBar = `Report sending ${filled}${unfilled}`;
      await loadingMessage.editText(loadingBar);
      await new Promise((resolve) => setTimeout(resolve, 500));
    }

    await loadingMessage.delete();

    const replyMessage = `${report.reportTop}\n\n👤 Rᴇᴘᴏʀᴛᴇʀ: ${report.reporter}\n🆔 Rᴇᴘᴏʀᴛᴇʀ ɪᴅ: ${report.reporterId}\n📜 Tʀᴀᴄᴋ ɪᴅ: ${report.trackId}\n\n💬 Rᴇᴘᴏᴛʀ ᴛᴇxᴛ: ${report.reportText}\n\n⌚ Rᴇᴘᴏʀᴛ ᴛɪᴍᴇ: ${report.reportTime}\n🗓️ Rᴇᴘᴏʀᴛ ᴅᴀᴛᴇ: ${report.reportDate}\n⛅ Rᴇᴘᴏʀᴛ ᴅᴀʏ: ${report.reportDay}`;
    await ctx.reply(replyMessage);

    const channelID = -1001904370879;
    const channelMessage = `Reporter: ${report.reporter}\nReporter ID: ${report.reporterId}\nTrack ID: ${report.trackId}\nReport Text: ${report.reportText}\nReport Time: ${report.reportTime}\nReport Date: ${report.reportDate}\nReport Day: ${report.reportDay}`;
    await bot.telegram.sendMessage(channelID, channelMessage);
  }
});

bot.launch().then(() => console.log('Bot started'));
