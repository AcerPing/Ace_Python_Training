# TODO: 抓取Medium.Com 的文章資料2021版，加入 Request Data 的觀念
import urllib.request as req
import json
#TODO: 建立連線網址
url="https://medium.com/_/graphql"

#TODO: 建立一個 Request 物件，附上 Request Headers 和 Request Data 的資訊
# Request Data → 請求的額外資料
requestData = {"operationName":"ExtendedFeedQuery","variables":{"items":[{"postId":"144ce6a376ae","topicId":""},{"postId":"e90431463924","topicId":""},{"postId":"a993c9e3e02f","topicId":""},{"postId":"6dbffd055814","topicId":""},{"postId":"517c64c2a3ac","topicId":""},{"postId":"be0a205af03d","topicId":""},{"postId":"2358f8451ef9","topicId":""},{"postId":"ab488fd553e2","topicId":""},{"postId":"d9b536f91c2","topicId":""},{"postId":"c763a7daa7e2","topicId":""},{"postId":"98baed2b4b7a","topicId":""},{"postId":"6f746ea7d850","topicId":""},{"postId":"ee577c98fc3a","topicId":""},{"postId":"b6360bed7b06","topicId":""},{"postId":"d0ef5ef6cd84","topicId":""},{"postId":"ffd33fe37dec","topicId":""},{"postId":"ac8e5bc9b455","topicId":""},{"postId":"5ad767af8564","topicId":""},{"postId":"3cab1c76f1db","topicId":""},{"postId":"8679bcb9fe81","topicId":""}]},"query":"query ExtendedFeedQuery($items: [ExtendedFeedItemOptions!]!) {\n  extendedFeedItems(items: $items) {\n    post {\n      ...PostListModulePostPreviewData\n      __typename\n    }\n    metadata {\n      topic {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PostListModulePostPreviewData on Post {\n  id\n  firstPublishedAt\n  readingTime\n  createdAt\n  mediumUrl\n  previewImage {\n    id\n    __typename\n  }\n  title\n  collection {\n    id\n    domain\n    slug\n    name\n    navItems {\n      url\n      __typename\n    }\n    logo {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    ...userUrl_user\n    __typename\n  }\n  visibility\n  isProxyPost\n  isLocked\n  ...HomeFeedItem_post\n  ...HomeReadingListItem_post\n  ...HomeTrendingModule_post\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment BookmarkButton_post on Post {\n  ...SusiClickable_post\n  ...WithSetReadingList_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment WithSetReadingList_post on Post {\n  ...ReadingList_post\n  __typename\n  id\n}\n\nfragment ReadingList_post on Post {\n  __typename\n  id\n  readingList\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  viewerClapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  shareKey\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    viewerIsEditor\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    isBlocking\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    viewerIsEditor\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  isMuting\n  __typename\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  viewerIsEditor\n  viewerIsMuting\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  viewerClapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  voterCount\n  viewerClapCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n  id\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerIsEditor\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    ...collectionUrl_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  username\n  id\n  name\n  imageId\n  mediumMemberAt\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  username\n  hasSubdomain\n}\n\nfragment HomeReadingListItem_post on Post {\n  id\n  title\n  creator {\n    id\n    name\n    username\n    ...UserAvatar_user\n    __typename\n  }\n  mediumUrl\n  createdAt\n  readingTime\n  collection {\n    id\n    name\n    navItems {\n      url\n      __typename\n    }\n    ...CollectionAvatar_collection\n    __typename\n  }\n  visibility\n  __typename\n}\n\nfragment HomeTrendingModule_post on Post {\n  id\n  ...HomeTrendingPostPreview_post\n  __typename\n}\n\nfragment HomeTrendingPostPreview_post on Post {\n  id\n  title\n  mediumUrl\n  readingTime\n  firstPublishedAt\n  ...PostPreviewAvatar_post\n  ...PostPresentationTracker_post\n  __typename\n}\n"}
request=req.Request(url,
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36",
        "Content-Type":"application/json"},
data=json.dumps(requestData).encode('utf-8'))

#TODO: 發出請求
with req.urlopen(request) as response:
    result = response.read().decode("utf8") #根據觀察，取得的資料是JSON格式
# print(result)

#TODO: 解析JSON格式的資料，取得每篇文章的標題
result = json.loads(result) #把原始的JSON資料解析成字典/列表的表示形式
# print(result) 
# print(result['data']['extendedFeedItems'][0]['post']['title']) #試著印出第一篇文章的標題
items = result['data']['extendedFeedItems']
# print(items)
for item in items:
    print(item['post']["title"])

