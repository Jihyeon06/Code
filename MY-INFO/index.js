// 관리
const Discord = require('discord.js');
const moment = require("moment"); // cmd에 'npm install moment' 실행
require("moment-duration-format"); // cmd에 'moment-duration-format' 실행
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

    if (message.content.startsWith('!정보')) {
        var d = new Date();
        var currentData = d.getFullYear() + "년 " + (d.getMonth() + 1) + "월 " + d.getDate() + "일 ";
        var currentTime = d.getHours() + "시 " + d.getMinutes() + "분 ";
        var user = message.author;
        var u_a = user.avatarURL({ format: 'png', dynamic: true, size: 1024 });
        var u_u = user.username;
        var u_d = `#${user.discriminator}`;
        var u_i = user.id;
        var u_p = user.presence.status;
        var u_c = moment.utc(message.guild.members.cache.get(user.id).user.createdAt).format("YYYY년, M월 D일");
        var u_j = moment.utc(message.guild.members.cache.get(user.id).user.joinedAt).format("YYYY년, M월 D일");
        var u_t = `${currentData + currentTime}`;
        if (u_p === 'online') {
            var userdate_embed = new (require("discord.js").MessageEmbed)()
            userdate_embed.setColor('#ffd014')
            userdate_embed.setAuthor(user.tag, user.avtar)
            userdate_embed.setThumbnail(u_a)
            userdate_embed.addField(`닉네임`, u_u, true)
            userdate_embed.addField(`태그`, u_d, true)
            userdate_embed.addField(`아이디`, u_i, true)
            userdate_embed.addField(`상태`, `온라인`, true)
            userdate_embed.addField(`가입한 날`, u_c)
            userdate_embed.addField(`들어온 날`, u_j)
            userdate_embed.setFooter("[ " + u_t + " ]")
            return message.channel.send(userdate_embed);
        } else if (u_p === 'idle') {
            var userdate_embed = new (require("discord.js").MessageEmbed)(body)
            userdate_embed.setColor('#ffd014')
            userdate_embed.setAuthor(user.tag, user.avtar)
            userdate_embed.setThumbnail(u_a)
            userdate_embed.addField(`닉네임`, u_u, true)
            userdate_embed.addField(`태그`, u_d, true)
            userdate_embed.addField(`아이디`, u_i, true)
            userdate_embed.addField(`상태`, `자리비움`, true)
            userdate_embed.addField(`가입한 날`, u_c)
            userdate_embed.addField(`들어온 날`, u_j)
            userdate_embed.setFooter("[ " + u_t + " ]")
            return message.channel.send(userdate_embed);	
        } else if (u_p === 'dnd') {
            var userdate_embed = new (require("discord.js").MessageEmbed)(body)
            userdate_embed.setColor('#ffd014')
            userdate_embed.setAuthor(user.tag, user.avtar)
            userdate_embed.setThumbnail(u_a)
            userdate_embed.addField(`닉네임`, u_u, true)
            userdate_embed.addField(`태그`, u_d, true)
            userdate_embed.addField(`아이디`, u_i, true)
            userdate_embed.addField(`상태`, `다른 용무 중`, true)
            userdate_embed.addField(`가입한 날`, u_c)
            userdate_embed.addField(`들어온 날`, u_j)
            userdate_embed.setFooter("[ " + u_t + " ]")
            return message.channel.send(userdate_embed);		
        } else if (u_p === 'offline') {
            var userdate_embed = new (require("discord.js").MessageEmbed)(body)
            userdate_embed.setColor('#ffd014')
            userdate_embed.setAuthor(user.tag, user.avtar)
            userdate_embed.setThumbnail(u_a)
            userdate_embed.addField(`닉네임`, u_u, true)
            userdate_embed.addField(`태그`, u_d, true)
            userdate_embed.addField(`아이디`, u_i, true)
            userdate_embed.addField(`상태`, `오프라인`, true)
            userdate_embed.addField(`가입한 날`, u_c)
            userdate_embed.addField(`들어온 날`, u_j)
            userdate_embed.setFooter("[ " + u_t + " ]")
            return message.channel.send(userdate_embed);
        }
    }
});
    
    client.login(Token);
    
    // 봇 제작 피리#8235
    // 이 메시지를 지우지 마시오.