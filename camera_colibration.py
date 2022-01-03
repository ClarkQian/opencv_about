import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:5].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('colibration/*.jpg')

counter = 0
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,5), None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        cv2.cornerSubPix(gray, corners, (11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (7,5), corners,ret)
        # img = cv2.resize(img, (400, 700))
        # cv2.imshow('img',img)
        # cv2.waitKey(0)
        counter += 1
        print(counter, len(images))
# todo this is the important code here to calculate the rotation matrix and t matrix
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(ret)
print(mtx)

    # from rotation vector to rotation matrix
    # rvecs2 = cv2.Rodrigues(rvecs[0])
    # rvecs3 = cv2.Rodrigues(rvecs2[0])



    # h, w = img.shape[:2]
    # newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    # undistort
    # mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
    # dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

    # crop the image
    # x, y, w, h = roi
    # dst = dst[y:y + h, x:x + w]
    # cv2.imshow('image', dst)
    # cv2.waitKey(0)

# cv2.destroyAllWindows()