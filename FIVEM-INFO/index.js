// 관리
const Discord = require('discord.js');
const request = require('request'); // cmd에 'npm install request' 실행
const cheerio = require('cheerio'); // cmd에 'npm install cheerio' 실행
const Token = `토큰`
const client = new Discord.Client();

// 관리
client.on('warn', console.warn);
client.on('error', console.error);
client.on('ready', () => console.log('I am ready!'));
client.on('disconnect', () => console.log('I disconnected!'));
client.on('reconnecting', () => console.log('I am disconnecting!'));

client.on('ready', () => {
    console.log(client.user.tag)
    console.log(client.user.id)
    console.log('\n봇이 준비 되었습니다.');
});

client.on('message', async message => {
    if (message.author.bot) return;

    if (message.content.startsWith('!서버인원')) {
        request(`http://서버주소/`, function (err, response, body) {
            const $ = cheerio.load(body)
            let players = $(".text-value") 
            var result = players[0].children[0].data;
            message.channel.send(`현재 서버 인원 : ${result}`)
            if (err) return console.log(err);
        })
    }
});
    
    client.login(Token);
    
    // 봇 제작 피리#8235
    // 이 메시지를 지우지 마시오.