// 관리
const Discord = require('discord.js');
const cheerio = require('cheerio');
const request = require('request');
const Token = `토큰`
const client = new Discord.Client();
const td = new Date();
const TimeData = td.getFullYear() + ". " + (td.getMonth() + 1) + ". " + td.getDate() + ". " + td.getHours() + ": " + td.getMinutes();

// 코로나 정보
let url3 = 'http://coronafact.org';
let url5 = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90';

request(url5, function(error, response, body) {
const $ = cheerio.load(body);
let cor2Arr = $(".num")
let corona5num = cor2Arr[1].children[0].data

request(url3, function(error, response, body) {
const $ = cheerio.load(body);
let cor1Arr = $(".timer.count-title.count-number.number")
let corona1num = cor1Arr[0].prev.next.attribs['data-to']
let corona2num = cor1Arr[1].prev.next.attribs['data-to']
let corona3num = cor1Arr[2].prev.next.attribs['data-to']
let corona4num = cor1Arr[3].prev.next.attribs['data-to']

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

    if (message.content.startsWith('!코로나')) {
        let url2 = 'http://coronafact.org';
        let url4 = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90';

        request(url4, function(error, response, body) {
        const $ = cheerio.load(body);
        let cor2Arr = $(".num")
        let corona5 = cor2Arr[1].children[0].data
        let corona5numb = corona5 - corona5num + 1

        request(url2, function(error, response, body) {
        const $ = cheerio.load(body);
        let cor1Arr = $(".timer.count-title.count-number.number")
        let corona1 = cor1Arr[0].prev.next.attribs['data-to']
        let corona2 = cor1Arr[1].prev.next.attribs['data-to']
        let corona3 = cor1Arr[2].prev.next.attribs['data-to']
        let corona4 = cor1Arr[3].prev.next.attribs['data-to']
        let corona1numb = corona1 - corona1num
        let corona2numb = corona2 - corona2num
        let corona3numb = corona3 - corona3num
        let corona4numb = corona4num - corona4
        var corona_embed = new (require("discord.js").MessageEmbed)()
        corona_embed.setAuthor("[ " + TimeData + " 기준 ]")
        corona_embed.setTitle("코로나19 현황")
        corona_embed.setThumbnail('https://i.imgur.com/sgRwnLJ.jpg')
        corona_embed.addField("**> 코로나 확진자**", corona1 + "명 ( ▲ " + corona1numb + "명 )", true)
        corona_embed.addField("**> 코로나 사망자**", corona2 + "명 ( ▲ " + corona2numb + "명 )", true)
        corona_embed.addField("**> 코로나 의심환자**", corona3 + "명 ( ▲ " + corona3numb + "명 )", true)
        corona_embed.addField("**> 코로나 검사중**", corona4 + "명 ( ▲ " + corona4numb + "명 )", true)
        corona_embed.addField("**> 코로나 격리해제**", corona5 + "명 ( ▲ " + corona5numb + "명 )", true)
        corona_embed.addField("**> 정보 지원**", "``coronafact.org``", true)
        corona_embed.setFooter("오늘도 찾아주셔서 감사합니다.")
        corona_embed.setColor('#B70000')
        message.channel.send(corona_embed)
        })
    })
    }
});
    
    client.login(Token);
    
    // 봇 제작 피리#8235
    // 이 메시지를 지우지 마시오.