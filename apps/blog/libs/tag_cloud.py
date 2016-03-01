# encoding: utf-8
__author__ = 'liuzhijun'


class TagCloud(object):
    MIN_FONT_SIZE = 12
    MAX_FONT_SIZE = 33
    FONT_SIZES = [MIN_FONT_SIZE, 15, 18, 21, 24, 27, 30, MAX_FONT_SIZE]
    COLORS = ['#ccc', "#adadad", '#8e8e8e', '#6f6f6f', '#4f4f4f', '#303030', '#111', '#000']

    def __init__(self, min_ref_count, max_ref_count):
        TagCloud.min_ref_count = min_ref_count
        # 如果最大标签和最小标签相等,那么认为两者的步长为0,所有标签取同样的font-size.
        if max_ref_count == min_ref_count:
            TagCloud.step = 0
        else:
            TagCloud.step = (TagCloud.MAX_FONT_SIZE - TagCloud.MIN_FONT_SIZE) / (max_ref_count - min_ref_count)

    def get_tag_font_size(self, tag_ref_count):
        font_size = TagCloud.MIN_FONT_SIZE + (tag_ref_count - TagCloud.min_ref_count) * TagCloud.step
        # 上面计算出来的font_size并不一定刚好是FONT_SIZES中的某个元素, 可以能某两个元素之间的某个值
        # 因此要取最接近FONT_SIZES中某个元素
        font_size = min(TagCloud.FONT_SIZES, key=lambda x: abs(font_size - x))
        return font_size

    def get_tag_color(self, tag_ref_count):
        return TagCloud.COLORS[(TagCloud.FONT_SIZES.index(self.get_tag_font_size(tag_ref_count)))]
