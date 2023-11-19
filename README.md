# nsfw-detecter-azfun

Azure cloud function version of [synodriver/unit_strange_code](https://github.com/synodriver/unit_strange_code)

![banner](tag/test.jpeg)

# API

> https://nsfwtag.azurewebsites.net/api/

> GET /api/nsfw?url=xxx or POST data to /api/nsfw

- 可选：size=224
- `url`参数可以传递多次，返回`List[Dict]`

```json
[
  [
    {
      "drawings": 0.9760909676551819,
      "hentai": 0.022929608821868896,
      "neutral": 0.0007943910895846784,
      "porn": 0.00016993124154396355,
      "sexy": 1.509424237156054e-5
    },
    {
      "drawings": 0.9663479924201965,
      "hentai": 0.032552674412727356,
      "neutral": 0.0008337266626767814,
      "porn": 0.0002492043131496757,
      "sexy": 1.6333018720615655e-5
    }
  ]
]
```

> GET /api/tag?url=xxx or POST data to /api/tag

- 可选：limit=0.7
- `url`参数可以传递多次，返回`List[Dict]`

```json
[
  {
    "2girls": 0.8092396259307861,
    "animal_costume": 0.93109530210495,
    "black_legwear": 0.764792263507843,
    "brown_eyes": 0.9567971229553223,
    "chibi": 0.7200598120689392,
    "dual_persona": 0.8917813897132874,
    "hand_on_hip": 0.8767830729484558,
    "letterboxed": 1.0,
    "long_hair": 0.9734611511230469,
    "open_mouth": 0.8793256282806396,
    "pillarboxed": 0.7099909782409668,
    "school_uniform": 0.85822993516922,
    "skirt": 0.9428402185440063,
    "smile": 0.9055765271186829,
    "thighhighs": 0.9884253740310669,
    "v": 0.9482945203781128,
    "rating:safe": 0.9913443326950073
  },
  {
    "1girl": 0.9998372793197632,
    "animal_ears": 0.9642201066017151,
    "black_background": 0.8620968461036682,
    "black_border": 0.8060356974601746,
    "blue_eyes": 0.8566339612007141,
    "blush": 0.7598142027854919,
    "circle_cut": 0.8044427633285522,
    "coat": 0.7726043462753296,
    "eyebrows_visible_through_hair": 0.7564899921417236,
    "fake_animal_ears": 0.950274646282196,
    "fur_trim": 0.9931351542472839,
    "hair_ornament": 0.9073508381843567,
    "hair_ribbon": 0.7280101180076599,
    "letterboxed": 1.0,
    "long_hair": 0.9948941469192505,
    "long_sleeves": 0.8017054796218872,
    "looking_at_viewer": 0.9293093085289001,
    "pillarboxed": 0.9984731078147888,
    "purple_hair": 0.9965977668762207,
    "ribbon": 0.7101029753684998,
    "solo": 0.9551721215248108,
    "sweater": 0.9029904007911682,
    "thighhighs": 0.9807195663452148,
    "very_long_hair": 0.929375946521759,
    "white_legwear": 0.8708877563476562,
    "tashkent_(azur_lane)": 0.9977080821990967,
    "rating:safe": 0.9979654550552368
  }
]
```
