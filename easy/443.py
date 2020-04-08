class Solution:
    def compress(self, chars: list) -> int:
        # 仅一个元素返回列表的长度
        if len(chars) == 1: return len(chars)
        # 增加一个辅助元素，把原始数组全部添加到新的表里面；pos指向的是新表要添加元素的位置（而且表示表长）
        chars.append('')
        count, pos = 1, 0
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                chars[pos] = chars[i - 1]
                pos += 1
                if count > 1:
                    for j in range(len(str(count))):
                        chars[pos + j] = str(count)[j]
                    pos += len(str(count))
                count = 1
            else:
                count += 1
        return pos  # 返回最终的表长


if __name__ == '__main__':
    sol = Solution()
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    output = sol.compress(chars)
    print(output)
    print(chars)

