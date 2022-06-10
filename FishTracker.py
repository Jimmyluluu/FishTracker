import cv2

cap = cv2.VideoCapture("oneFishTest.mp4")

# 背景分離
object_detector = cv2.createBackgroundSubtractorMOG2(history=0, varThreshold=0)

# 建立追蹤物件
# tracker = EuclideanDistTracker()

while True:

    ret, frame = cap.read()

    # 建立追蹤物件
    mask = object_detector.apply(frame)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    # 找尋物體輪廓
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5:
            x, y, w, h = cv2.boundingRect(cnt)
            # cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            # x y 是頂點座標
            # w h 是物件的長及寬
            # x + w, y + h 是對象頂點座標
            # 加入文字
            cv2.putText(frame, "Fish", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))
            detections.append([x, y, w, h])

    # 物件追蹤2
    # boxes_ids = tracker.update(detections)
    # print(boxes_ids)

    print(detections)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
