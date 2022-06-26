// 관리
const Discord = require('discord.js');
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

    if (message.content.startsWith('!피드백')) {
        const feedback_m = message.content.length
        const feedback_ms = message.content.substring(5)
    
        if (feedback_m === '4' || feedback_m < '9') {
            message.channel.send("```피드백 메세지는 3글자를 넘겨야 보낼 수 있습니다.```")
        } else {
            let filter = (reaction, user) => (reaction.emoji.name === '⭕' || reaction.emoji.name === '❌') && user.id === message.author.id;

            var FD_embed = new (require("discord.js").MessageEmbed)()
            FD_embed.setColor('#ED0000')
            FD_embed.setTitle('정말 관리자에게 피드백을 보내시겠습니까?')
            FD_embed.setDescription("보내려면 ⭕, 취소하려면 ❌를 눌러주세요.\n15초 이내로 보내주세요.")
            FD_embed.setFooter("오늘도 찾아주셔서 감사합니다.")

            message.channel.send(FD_embed).then(msg => {
                msg.react('⭕');
                msg.react('❌');

                msg.awaitReactions(filter, {
                    max: 1,
                    time: 15000,
                    errors: ['time']
                }).then(collected => {
                    const reaction = collected.first();

                    switch (reaction.emoji.name) {
                        case '⭕':
                            try {
                            client.users.cache.get("당신의 유저 ID").send(`<${message.author.id}>님의 메시지 입니다.\n태그 : ${message.author.tag}\n[ ${feedback_ms} ]`);

                            var FD1_embed = new (require("discord.js").MessageEmbed)()
                            FD1_embed.setColor('#ED0000')
                            FD1_embed.setTitle("성공적으로 개발자에게 피드백 메세지를 전송했습니다.")
                            FD1_embed.setDescription("전송 내용 : `" + feedback_ms + "`")
                            FD1_embed.setFooter("오늘도 찾아주셔서 감사합니다.")
                            message.channel.send(FD1_embed)
                            break;
                            } catch (err) {
                                message.channel.send("오류가 발생했습니다.\n`" + err + "`")
                            }
                            break;
                        case '❌':
                            try {
                            var FD2_embed = new (require("discord.js").MessageEmbed)()
                            FD2_embed.setColor('#ED0000')
                            FD2_embed.setTitle("피드백 전송을 취소하였습니다.")
                            FD2_embed.setDescription("전달된 내용은 없습니다.")
                            FD2_embed.setFooter("오늘도 찾아주셔서 감사합니다.")
                            message.channel.send(FD2_embed)
                            break;
                            } catch (err) {
                                message.channel.send("오류가 발생했습니다.\n`" + err + "`")
                            }
                            break;
                    }
                }).catch(collected => {
                    
                });

            });
        }
    }
});
    
    client.login(Token);
    
    // 봇 제작 피리#8235
    // 이 메시지를 지우지 마시오.