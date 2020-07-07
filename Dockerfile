# parameters
ARG REPO_NAME="mooc-exercises"

# ==================================================>
# ==> Do not change this code
ARG ARCH=arm32v7
ARG MAJOR=daffy
ARG BASE_TAG=${MAJOR}-${ARCH}
ARG BASE_IMAGE=dt-core 
#dt-ros-commons

# define base image
FROM duckietown/${BASE_IMAGE}:${BASE_TAG}

# define repository path
ARG REPO_NAME
ARG REPO_PATH="${CATKIN_WS_DIR}/src/dt-core"
#${REPO_NAME}"
WORKDIR "${REPO_PATH}"

# create repo directory
RUN mkdir -p "${REPO_PATH}"

# copy dependencies files only
COPY ./dockerimage/dependencies-apt.txt "${REPO_PATH}/"
COPY ./dockerimage/dependencies-py.txt "${REPO_PATH}/"

COPY ./notebook/exercise.ipynb "${REPO_PATH}/"

# install apt dependencies
RUN apt-get update \
  && apt-get install -y git \
  && apt-get install -y --no-install-recommends \
    $(awk -F: '/^[^#]/ { print $1 }' dependencies-apt.txt | uniq) \
  && rm -rf /var/lib/apt/lists/*

# install python dependencies
RUN pip install -r ${REPO_PATH}/dependencies-py.txt

     

# create the packages
RUN mkdir -p "${REPO_PATH}/packages" \
    && cd ${REPO_PATH}/packages \
    && git clone https://github.com/viciopoli01/MOOCexercisesBones.git
#    && sudo mv MOOCexercisesBones/mooc ${REPO_PATH}/packages \
#    && python MOOCexercisesBones/clone.py \
#    && sudo rm -rf MOOCexercisesBones


# copy the source code
ADD . "${REPO_PATH}/"




# build packages
#RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
#  catkin build \
#    --workspace ${CATKIN_WS_DIR}/
#
## define launch script
#ENV LAUNCHFILE "${REPO_PATH}/launch.sh"
#
## define command
#CMD ["bash", "-c", "${LAUNCHFILE}"]
## <== Do not change this code
# <==================================================

# maintainer
LABEL maintainer="<YOUR_FULL_NAME> (<YOUR_EMAIL_ADDRESS>)"