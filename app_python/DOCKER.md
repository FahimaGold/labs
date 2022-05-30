# Best practices

In this file, you find the most recommended best practices for docker, here are some:

- Using mutli-stage building: building in a pre-final image and then copy only necessary artifacts to the final image. by avoiding adding temporary build files and other files which are not needed for image, for the purpose of reducing the final image size.
- Usinging a linter for the `Dockerfile` such as Haskell Dockerfile Linter (Hadolint).
- Avoiding to install uncessary packages: As extra packages will increase the image size.
- Decoupling applications: As each container should include only one concern (One container per service, another one for the frontend, etc), which makes it easy to scale horizontally and to reuse containers.
- Minimizing the number of layers: as it is a way to ensure that the images are more performant.
- Sorting multi-line arguments: It is preferable to sort them alphanumerically in order to avoid duplication of packages, and for ease of read and review.
- Leverage build cache: As docker has its own cache, before creating a new image during build, it will check if there is already an exisiting image that it can use.
- Using `COPY` instead of `ADD`: Although both `COPY` and `ADD` do similar actions, it is preferable to use `COPY` whenver possible as it is more explicit, and `ADD` is used for fetching remoe files through URLs or tar files.
- Managing pipes well: When using pipes, which are represented by `|` in commands, as the command before the pipe delivers its output to the one after the pipe, it is better to consider the case that when the first command fails, what comes after the pipe fails as well and it does not pursue exeuction. Therefore, prepand the first command before the pipe by `set -o pipefail &&`. 
- Exposing only needed ports: Avoid exposing uncessary ports to the container such as `SSH` in order to minimize security risks.
- Using `VOLUME` for mutable parts of the image: This instruction is used to expose any database or configuration storage.
- Creating ephemeral containers: It means creating containers that can be stopped, destroyed, and rebuilt.
- Understanding build context: The build context is the current working directory. It is recommend to avoid using `.` as build context since it risks copying confidential or uncessary files. Instead, create a sub-folder of the files that you need to copy inside the container.
- Image scanning: It is important to scan images before running containers in order to detect any potential problems. The image should be scanned in the CI pipeline, before pushing it to the registry.
- Signing images and verifying signitures: In order to ensure the integrity of the image.
- Making executables owned by root and not writable: Exectuables should be owned only by root, even if they can be executed by other users, and they should not be writable in order to prevent many security risks. 
- Rootless containers: In many cases, containers need to be exectued by non-root users. Therefore, include the `USER` instruction to change the default UID to a non-root user.