package helper;

import java.util.Random;

/**
 * This class simulates a version control system where versions are checked
 * to determine if they are "bad" or not. The "bad" version is randomly
 * generated when an instance of the class is created.
 */
public abstract class VersionControl {
    private final int culpritVersion;
    public VersionControl() {
        culpritVersion = new Random().nextInt(100);
    }
    public boolean isBadVersion(int version) {
        return version >= culpritVersion;
    }
}
