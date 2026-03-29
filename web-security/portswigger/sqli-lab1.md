# PortSwigger SQL注入 Lab 1

## 题目
WHERE子句中的SQL注入漏洞，允许检索隐藏数据

## 目标
显示所有产品，包括未发布的

## 解题步骤

1. 点击"礼品"分类，URL为 `?category=Gifts`
2. 修改URL为 `?category=Gifts' OR 1=1--`
3. 回车，看到"恭喜你，你解决了实验题！"

## Payload
## 原理
- `'` 闭合原SQL字符串
- `OR 1=1` 永真条件
- `--` 注释掉后面代码

## 完成时间
2025-03-30
