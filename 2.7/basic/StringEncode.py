# -*- coding: utf-8 -*-

print u'测试中文配置'
print (u'中文'.encode('utf-8'))

print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')
print len(u'中文'.encode('utf-8'))

# 文本的格式化方式
print 'Hello %s' % 'world'
print 'he micale %d, %s, %1.2f, %x' %(100, 'string content', 1.0, 100)
print '%10d %%' % 3