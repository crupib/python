pantry = [ ('avocados', 1.25), ('bananas', 2.5), ('cherries', 15),]
for i, (item, count) in enumerate(pantry):
     before = '#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count))
     print(before)
     after = '#%(loop)d: %(item)-10s = %(count)d' % {
           'loop': i + 1,
           'item': item.title(),
           'count': round(count),
     }
     print(after)
     print(item.title())
