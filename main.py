from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, TemplateSendMessage, ConfirmTemplate,
    MessageAction, URIAction, ButtonsTemplate, PostbackAction, Postback, PostbackEvent,
    QuickReply, QuickReplyButton, ImageSendMessage
)

import json

app = Flask(__name__)

line_bot_api = LineBotApi(
    'nbE0Yqi3KGYDpWH579IgAtS1ggxub+PUUgy0tUvNlkKAfIoRdo4D2GOiaPOQgqA6wr47BQdZ/6S4C'
    '/uhLmphZ2EpCs7xHhRwVC2kzpmdwVIyAnWRxdxEw3JKJvl1uY64mLntrp2GqPwUJccqeEc4owdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('784899c6df4a550a6b1d11f2fb5ad363')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 歡迎訊息


@handler.add(FollowEvent)
def handle_follow(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    with open("namelist.txt", "a") as myfile:
        myfile.write(
            json.dumps(
                vars(user_profile)
            )
        )
        myfile.write("\r")

    follow_text_send_message = TextSendMessage(
        "Hello，\n"
        "我是「食米不知米價」機器人，\n"
        "對你生活周遭的食衣住行開銷，\n"
        "你到底了解了多少呢？\n"
        "\n"
        "先試試看你對甚麼領域有興趣吧！"
    )

# 詢問喜好

    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://images.plurk.com/64ZDVCsKT7rRdkODQ9xWnN.jpg',
            title='我想猜這個',
            text='選一個有興趣的領域吧！',
            actions=[
                PostbackAction(
                    label='3c',
                    display_text='我想猜猜3c產品',
                    data='theme=1'
                ),
                PostbackAction(
                    label='電玩',
                    display_text='我想猜猜看電玩價格',
                    data='theme=2'
                ),
                PostbackAction(
                    label='甜點',
                    display_text='我想猜猜甜點價位',
                    data='theme=3'
                )
            ]
        )
    )

    line_bot_api.reply_message(event.reply_token, [follow_text_send_message,
                                                   buttons_template_message])


# 詢問經驗


@handler.add(PostbackEvent)
def postback_lvl1(event):
    if PostbackEvent. == 'theme=1':
        confirm_template_message = TemplateSendMessage(
            alt_text='你有用過iPhone嗎？',
            template=ConfirmTemplate(
                text='想了解你使用iPhone的經驗',
                actions=[
                    PostbackAction(
                        label='有',
                        display_text='我有用過iPhone',
                        data='theme=1&have=1'
                    ),
                    PostbackAction(
                        label='沒有',
                        display_text='我沒有用過iPhone',
                        data='theme=1&have=0'
                    )
                ]
            )
        )
        # text_quickreply1 = QuickReplyButton(action=MessageAction(label="有", text="我有iPhone"))
        # text_quickreply2 = QuickReplyButton(action=MessageAction(label="沒有", text="我沒有iPhone"))
        #
        # quick_reply_array = QuickReply(items=[text_quickreply1, text_quickreply2])
        #
        # reply_text_message = TextSendMessage("請問您是否持有iPhone手機？", quick_reply=quick_reply_array)
        #
        line_bot_api.reply_message(event.reply_token, confirm_template_message)

    elif event.message.text == '我想猜猜電玩產品':
        text_quickreply1 = QuickReplyButton(action=MessageAction(label="有", text="我有Switch"))
        text_quickreply2 = QuickReplyButton(action=MessageAction(label="沒有", text="我沒有Switch"))

        quick_reply_array = QuickReply(items=[text_quickreply1, text_quickreply2])

        reply_text_message = TextSendMessage("請問您是否持有Switch主機？", quick_reply=quick_reply_array)

        line_bot_api.reply_message(event.reply_token, [reply_text_message])

    elif event.message.text in {"我有iPhone", "我沒有iPhone"}:
        price_asking = TextSendMessage("猜猜看現在一台\n"
                                       "iPhone 11 Pro 64G\n"
                                       "售價大概多少錢呢？")
        line_bot_api.reply_message(event.reply_token, price_asking)

    elif event.message.text in {"我有Switch", "我沒有Switch"}:
        price_asking = TextSendMessage("猜猜看現在一台\n"
                                       "Switch紅藍款 (主機only)\n"
                                       "售價大概多少錢呢？")
        line_bot_api.reply_message(event.reply_token, price_asking)

    # elif event.message.text == '我想猜猜甜點價位':
    #     text_quickreply1 = QuickReplyButton(action=MessageAction(label="喜歡", text="我喜歡吃甜點"))
    #     text_quickreply2 = QuickReplyButton(action=MessageAction(label="不喜歡", text="我不喜歡吃甜點"))
    #
    #     quick_reply_array = QuickReply(items=[text_quickreply1, text_quickreply2])
    #
    #     reply_text_message = TextSendMessage("請問您是否喜歡吃甜點？", quick_reply=quick_reply_array)
    #
    #     line_bot_api.reply_message(event.reply_token, [reply_text_message])

# TODO 問題2 購買意願

# TODO 估計價錢、回傳高估or低估 要用postback


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     if event.message.text == "我有iPhone" or "我沒有iPhone":
#         price_asking = TextSendMessage("猜猜看現在一台\n"
#                                        "iPhone 11 Pro 64G\n"
#                                        "售價大概多少錢呢？")
#         line_bot_api.reply_message(event.reply_token, price_asking)
#     elif event.message.text in {"我有Switch", "我沒有Switch"}:
#         price_asking = TextSendMessage("猜猜看現在一台\n"
#                                        "Switch紅藍款 (主機only)\n"
#                                        "售價大概多少錢呢？")
#         line_bot_api.reply_message(event.reply_token, price_asking)

    # elif event.message.text == "我喜歡吃甜點" or "我不喜歡吃甜點":
    #     pass # todo 甜點資料
    #     line_bot_api.reply_message(event.reply_token, [price_asking])

# TODO 回傳統計圖表

#
# @handler.add(MessageEvent, message=TextMessage)
# def handle_image_message(event):
#     static_chart = ImageSendMessage(
#         original_content_url="./chart.png",
#         preview_image_url=""
#     )
#     line_bot_api.reply_message(event.reply_token, [static_chart])

# TODO 圖文選單


if __name__ == "__main__":
    app.run()
