pantry = [ ('avocados', 1.25), ('bananas', 2.5), ('cherries', 15),]
for i, (item, count) in enumerate(pantry):
     old_style = '#%d: %-10s = %d' % (
            i + 1,
            item.title(),
            round(count))
     new_style = '#{}: {:<10s} = {}'.format(
            i + 1,
            item.title(),
            round(count))
     print(old_style)
     print(new_style)
