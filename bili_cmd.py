import argparse
import asyncio
from lighting_downloader import Downloader


async def main(args):
    d = Downloader(videos_dir=args.dir, video_concurrency=args.max_con, sess_data=args.cookie)
    if args.method == 'get_series':
        await d.get_series(args.key, quality=args.q)
    elif args.method == 'get_video':
        await d.get_video(args.key, quality=args.q)
    elif args.method == 'get_up':
        await d.get_up_videos(args.key, quality=args.q, total=args.num, order=args.order, keyword=args.keyword)
    elif args.method == 'get_cate':
        await d.get_cate_videos(
            args.key, quality=args.q, num=args.num, order=args.order, keyword=args.keyword, days=args.days)
    else:
        print(f'{args.method}不能识别，请使用正确的方法名')
    await d.aclose()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='⚡️Lighting-bilibili-download ⚡️快如闪电的bilibili下载工具')
    parser.add_argument('method', type=str, help='get_series：获取整个系列的视频（包括多p投稿，动漫，电视剧，电影，纪录片），也可以下载单个视频 '
                                                 'get_video：获取特定的单个视频，在用户不希望下载系列其他视频的时候可以使用'
                                                 'get_up：获取某个up的所有投稿视频，支持数量选择，关键词搜索，排序'
                                                 'get_cate：获取分区视频，支持数量选择，关键词搜索，排序')
    parser.add_argument('key', type=str,
                        help='视频url，如果是获取整个系列，提供系列中任意一集视频的url即可，如果使用get_up，则在该位置填写b站用户id，如果使用get_cate，则在该位置填写分区名称')
    parser.add_argument('-q', type=int, default=0, help='视频画面质量，默认0为最高画质，越大画质越低，超出范围时自动选最低画质')
    parser.add_argument('-max_con', type=int, default=5, help='控制最大同时下载的视频数量，理论上网络带宽越高可以设的越高')
    parser.add_argument('-cookie', type=str, default='', help='有条件的用户可以提供大会员的SESSDATA来下载会员视频')
    parser.add_argument('-dir', type=str, default='videos', help='文件的下载目录，默认当前路径下的videos文件夹下，不存在会自动创建')

    parser.add_argument('-num', type=int, default=10, help='下载前多少个投稿，仅get_up，get_cate时生效')
    parser.add_argument('-order', type=str, default='pubdate',
                        help='何种排序，click播放数，scores评论数，stow收藏数，coin硬币数，dm弹幕数, 仅get_up, get_cate时生效')
    parser.add_argument('-keyword', type=str, default='', help='搜索关键词， 仅get_up, get_cate时生效')

    parser.add_argument('-days', type=int, default=7, help='过去days天中的结果，仅get_up, get_cate时生效')

    asyncio.run(main(parser.parse_args()))
